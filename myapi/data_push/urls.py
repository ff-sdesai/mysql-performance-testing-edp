# urls.py
from django.urls import path
from .views.get_devices import get_devices
from .views.post_devices import post_devices

urlpatterns = [
    path('api/devices/', get_devices, name='get_devices'),  # GET request
    path('api/devices/add/', post_devices, name='post_devices'),  # POST request
]
