from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer
from rest_framework import status


@api_view(['POST'])
def push_data(request):
    """
    API view to push data into the 'customers' table.
    Accepts JSON data with fields: first_name, last_name, email, gender, ip_address
    """
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data, many=True)  # many=True for list of objects
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_customers(request):
    """
    API view to retrieve all customers (data) from the database.
    """
    data = Data.objects.all()  # Retrieve all data from the 'customers' table
    serializer = DataSerializer(data, many=True)  # Serialize the data
    return Response(serializer.data)  # Return the serialized data as JSON
