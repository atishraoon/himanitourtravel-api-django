from django.urls import path
from .views import *


urlpatterns = [
    path('Destination/', DestinationListAPIView.as_view(), name='destination'),
    path('contact/', send_contact_email, name='send_contact_email'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),

]

