from django.urls import path
from .views import push_data, get_customers

urlpatterns = [
    path('push/', push_data, name='push_data'),
    path('customers/', get_customers, name='get_customers'),  # Add the GET endpoint
]
