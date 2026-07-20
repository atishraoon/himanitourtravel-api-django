from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import status as http_status
from .utils import send_subscription_confirmation_email , send_travel_inquiry_confirmation_email


class PackageLookupAPIView(APIView):
    """
    POST /api/package-lookup/
    Body: { "full_name": "John Doe", "email": "john@example.com" }

    Returns the package_detail, total_package_amount, current_amount_to_pay,
    previous_amount_paid and status for that person.
    """

    def post(self, request):
        req_serializer = PackageLookupRequestSerializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)

        full_name = req_serializer.validated_data["full_name"]
        email = req_serializer.validated_data["email"]

        # case-insensitive match on both fields, latest record first
        record = (
            PackagePayment.objects.filter(
                full_name__iexact=full_name, email__iexact=email
            )
            .order_by("-created_at")
            .first()
        )

        if not record:
            return Response(
                {"detail": "No matching package found for this name and email."},
                status=http_status.HTTP_404_NOT_FOUND,
            )

        data = PackagePaymentDetailSerializer(record).data
        return Response(data, status=http_status.HTTP_200_OK)
 
class DestinationListAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# send email form site
@api_view(['POST'])
def send_contact_email(request):
    data = request.data

    try:
        # Required fields
        full_name = data["full_name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]

        # Optional field
        travel_date = data.get("travel_date")

        # Get destination
        destination_slug = data["preferred_destination"]
        
        destination = Destination.objects.get(slug=destination_slug)

        # Save to database
        inquiry = TravelInquiry.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            preferred_destination=destination,
            travel_date=travel_date if travel_date else None,
            message=message,
        )


        # Send email to bussiness mail
        send_mail(
            subject=f"New Travel Inquiry - {destination.name}",
            message=f"""
New Travel Inquiry

Name: {inquiry.full_name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Preferred Destination: {destination.name}
Travel Date: {inquiry.travel_date or 'Not provided'}

Message:
{inquiry.message}  
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["noreply@himanitourtravel.com"],  # Replace with your business email
            fail_silently=False,
        )

        # send email to user or coustomer
        send_travel_inquiry_confirmation_email(
            email=email,
            full_name=full_name,
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Inquiry submitted successfully."
            },
            status=status.HTTP_201_CREATED,
        )

    except KeyError as e:
        return JsonResponse(
            {"error": f"Missing required field: {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Destination.DoesNotExist:
        return JsonResponse(
            {"error": "Selected destination does not exist."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

 
        
# subscribe user and send confirmation mail
class Subscribe(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '').strip()
        phone_no = request.data.get('phone_no', '').strip()
        
        if not email:
            return Response(
                {'error': 'Email is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {'error': 'Enter a valid email address'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if email already exists
        if Subscriber.objects.filter(email=email).exists():
            return Response(
                {'error': 'This email is already subscribed'},
                status=status.HTTP_409_CONFLICT
            )
        
        subscriber = Subscriber.objects.create(email=email, phone_no=phone_no)
        serializer = SubscriberSerializer(subscriber)
 
        send_subscription_confirmation_email(email)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


 


