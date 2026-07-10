from rest_framework import serializers
from .models import Subscriber , Destination

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