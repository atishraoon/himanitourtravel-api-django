from django.urls import path
from .views import *
from .razorpay_integration import (
    CreateRazorpayOrderAPIView,
    VerifyRazorpayPaymentAPIView,
    RazorpayWebhookAPIView,
)


urlpatterns = [
    path('Destination/', DestinationListAPIView.as_view(), name='destination'),
    path('contact/', send_contact_email, name='send_contact_email'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),

    path("package-lookup/", PackageLookupAPIView.as_view(), name="package-lookup"),
    path(
        "razorpay/create-order/",
        CreateRazorpayOrderAPIView.as_view(),
        name="razorpay-create-order",
    ),
    path(
        "razorpay/verify-payment/",
        VerifyRazorpayPaymentAPIView.as_view(),
        name="razorpay-verify-payment",
    ),
    path(
        "razorpay/webhook/",
        RazorpayWebhookAPIView.as_view(),
        name="razorpay-webhook",
    ),

]

