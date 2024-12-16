from django.urls import path
from .views import devices_api

urlpatterns = [
    path('api/devices/', devices_api, name='devices_api'),
]
