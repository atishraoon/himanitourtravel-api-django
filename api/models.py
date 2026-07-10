from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TravelInquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    preferred_destination = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inquiries"
    )

    travel_date = models.DateField(blank=True, null=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.preferred_destination} - {self.phone}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    phone_no = models.CharField(
        max_length=20,
        blank=False,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        verbose_name="Phone Number",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Subscriber from {self.email} / {self.phone_no} "

    class Meta:
        ordering = ['-created_at']


