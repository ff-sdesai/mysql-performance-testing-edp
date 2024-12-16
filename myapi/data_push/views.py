import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from .serializers import DeviceSerializer

@api_view(['GET', 'POST'])
def devices_api(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Check if request data contains `bulk: True`
        if request.data.get('bulk') is True:
            try:
                # Read data from local CSV file
                with open('data_push/data/devices_small.csv', mode='r') as file:
                    reader = csv.DictReader(file)
                    data_list = [row for row in reader]

                # Serialize and save data
                serializer = DeviceSerializer(data=data_list, many=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except FileNotFoundError:
                return Response(
                    {"error": "Local file data.csv not found."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                return Response(
                    {"error": f"An unexpected error occurred: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        elif not request.data:  # Handle empty request data
            return Response(
                {"error": "No data provided and 'bulk' key not set to True."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Process request data normally if `bulk` is not True
            serializer = DeviceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
