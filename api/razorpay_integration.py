"""
Razorpay integration for the PackagePayment model.

Flow:
1. Frontend calls CreateRazorpayOrderAPIView with the PackagePayment id
   (or full_name+email) and gets back an `order_id` + Razorpay `key`.
2. Frontend opens Razorpay Checkout using that order_id.
3. On success, Razorpay returns razorpay_payment_id, razorpay_order_id,
   razorpay_signature to the frontend, which POSTs them to
   VerifyRazorpayPaymentAPIView.
4. We verify the signature server-side, then update the record's
   previous_amount_paid / status.
5. (Recommended) Also set up a Razorpay webhook pointing at
   RazorpayWebhookAPIView so payment confirmation doesn't rely solely
   on the frontend calling step 4 (covers dropped connections, etc).
"""

import razorpay
import hmac
import hashlib
import json

from decimal import Decimal
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status

from .models import PackagePayment
from .utils import send_payment_success_email

# Single shared client instance
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)


# ---------------------------------------------------------------------
# 1. CREATE ORDER
# ---------------------------------------------------------------------
class CreateRazorpayOrderAPIView(APIView):
    """
    POST /api/razorpay/create-order/
    Body: { "package_id": 1 }

    Creates a Razorpay Order for `current_amount_to_pay` and returns
    the order_id the frontend needs to open Razorpay Checkout.
    """

    def post(self, request):
        package_id = request.data.get("package_id")
        if not package_id:
            return Response(
                {"detail": "package_id is required."},
                status=http_status.HTTP_400_BAD_REQUEST,
            )

        try:
            package = PackagePayment.objects.get(id=package_id)
        except PackagePayment.DoesNotExist:
            return Response(
                {"detail": "Package not found."},
                status=http_status.HTTP_404_NOT_FOUND,
            )

        if package.status == PackagePayment.STATUS_COMPLETE:
            return Response(
                {"detail": "This package is already fully paid."},
                status=http_status.HTTP_400_BAD_REQUEST,
            )

        # Razorpay expects amount in paise (smallest currency unit)
        amount_paise = int(package.current_amount_to_pay * 100)

        razorpay_order = razorpay_client.order.create(
            {
                "amount": amount_paise,
                "currency": "INR",
                "receipt": f"package_{package.id}",
                "payment_capture": 1,  # auto-capture on success
                "notes": {
                    "package_id": str(package.id),
                    "full_name": package.full_name,
                    "email": package.email,
                },
            }
        )

        # Save the order id so we can cross-check it during verification
        package.razorpay_order_id = razorpay_order["id"]
        package.status = PackagePayment.STATUS_ONGOING
        package.save(update_fields=["razorpay_order_id", "status"])

        return Response(
            {
                "order_id": razorpay_order["id"],
                "amount": amount_paise,
                "currency": "INR",
                "key": settings.RAZORPAY_KEY_ID,
                "package_id": package.id,
                "name": package.full_name,
                "email": package.email,
            },
            status=http_status.HTTP_200_OK,
        )


# ---------------------------------------------------------------------
# 2. VERIFY PAYMENT (called by frontend after Checkout success)
# ---------------------------------------------------------------------
class VerifyRazorpayPaymentAPIView(APIView):
    """
    POST /api/razorpay/verify-payment/
    Body: {
        "razorpay_order_id": "...",
        "razorpay_payment_id": "...",
        "razorpay_signature": "..."
    }
    """

    def post(self, request):
        data = request.data
        order_id = data.get("razorpay_order_id")
        payment_id = data.get("razorpay_payment_id")
        signature = data.get("razorpay_signature")

        if not all([order_id, payment_id, signature]):
            return Response(
                {"detail": "Missing razorpay order/payment/signature fields."},
                status=http_status.HTTP_400_BAD_REQUEST,
            )

        try:
            package = PackagePayment.objects.get(razorpay_order_id=order_id)
        except PackagePayment.DoesNotExist:
            return Response(
                {"detail": "No package matches this order_id."},
                status=http_status.HTTP_404_NOT_FOUND,
            )

        # Verify signature using Razorpay SDK's utility
        try:
            razorpay_client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": order_id,
                    "razorpay_payment_id": payment_id,
                    "razorpay_signature": signature,
                }
            )
        except razorpay.errors.SignatureVerificationError:
            return Response(
                {"detail": "Payment signature verification failed."},
                status=http_status.HTTP_400_BAD_REQUEST,
            )

        _mark_package_paid(package, payment_id, signature)

        return Response(
            {"detail": "Payment verified successfully.", "status": package.status},
            status=http_status.HTTP_200_OK,
        )


# ---------------------------------------------------------------------
# 3. WEBHOOK (recommended — source of truth, doesn't depend on frontend)
# ---------------------------------------------------------------------
class RazorpayWebhookAPIView(APIView):
    """
    POST /api/razorpay/webhook/

    Configure this URL in Razorpay Dashboard -> Settings -> Webhooks,
    subscribed to the 'payment.captured' event, with a webhook secret
    set in settings.RAZORPAY_WEBHOOK_SECRET.
    """

    # Webhooks aren't authenticated the normal way, so skip DRF auth/CSRF
    authentication_classes = []
    permission_classes = []

    @csrf_exempt
    def post(self, request):
        webhook_secret = settings.RAZORPAY_WEBHOOK_SECRET
        signature = request.headers.get("X-Razorpay-Signature", "")
        body = request.body  # raw bytes, required for signature check

        expected_signature = hmac.new(
            key=webhook_secret.encode(),
            msg=body,
            digestmod=hashlib.sha256,
        ).hexdigest()

        if not hmac.compare_digest(expected_signature, signature):
            return Response(
                {"detail": "Invalid webhook signature."},
                status=http_status.HTTP_400_BAD_REQUEST,
            )

        payload = json.loads(body)
        event = payload.get("event")

        if event == "payment.captured":
            payment_entity = payload["payload"]["payment"]["entity"]
            order_id = payment_entity["order_id"]
            payment_id = payment_entity["id"]

            try:
                package = PackagePayment.objects.get(razorpay_order_id=order_id)
            except PackagePayment.DoesNotExist:
                # Nothing to update — acknowledge anyway so Razorpay
                # doesn't keep retrying.
                return Response(status=http_status.HTTP_200_OK)

            if package.status != PackagePayment.STATUS_COMPLETE:
                _mark_package_paid(package, payment_id, signature)

        return Response(status=http_status.HTTP_200_OK)


# ---------------------------------------------------------------------
# Shared helper
# ---------------------------------------------------------------------
def _mark_package_paid(package: PackagePayment, payment_id: str, signature: str):
    """
    Moves current_amount_to_pay into previous_amount_paid and marks the
    package complete (or leaves it ongoing if you support partial/
    installment payments — adjust this logic to your business rules).
    """
    package.razorpay_payment_id = payment_id
    package.razorpay_signature = signature

    # capture what was actually paid in THIS transaction, before we
    # overwrite current_amount_to_pay below - needed for the email
    amount_paid_now = package.current_amount_to_pay

    package.previous_amount_paid = (
        package.previous_amount_paid + package.current_amount_to_pay
    )

    if package.previous_amount_paid >= package.total_package_amount:
        package.status = PackagePayment.STATUS_COMPLETE
        package.current_amount_to_pay = Decimal("0")
    else:
        # partial payment received — still ongoing, update remaining due
        package.current_amount_to_pay = (
            package.total_package_amount - package.previous_amount_paid
        )
        package.status = PackagePayment.STATUS_ONGOING

    package.save(
        update_fields=[
            "razorpay_payment_id",
            "razorpay_signature",
            "previous_amount_paid",
            "current_amount_to_pay",
            "status",
        ]
    )

    send_payment_success_email(package, amount_paid_now)