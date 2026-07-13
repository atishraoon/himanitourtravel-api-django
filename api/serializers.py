from rest_framework import serializers
from .models import Subscriber , Destination , PackagePayment



class PackageLookupRequestSerializer(serializers.Serializer):
    """Used to validate the incoming POST body: full_name + email."""
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()


class PackagePaymentDetailSerializer(serializers.ModelSerializer):
    """What we send back once we find the matching record."""

    class Meta:
        model = PackagePayment
        fields = [
            "id",
            "full_name",
            "email",
            "package_detail",
            "total_package_amount",
            "current_amount_to_pay",
            "previous_amount_paid",
            "status",
        ]

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone_no','created_at']
        read_only_fields = ['created_at']


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = [
            "name",
        ]