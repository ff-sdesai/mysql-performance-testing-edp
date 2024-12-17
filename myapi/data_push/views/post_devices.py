# views/post_devices.py
import csv
import time
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from data_push.models import Device
from data_push.serializers import DeviceSerializer

@api_view(['POST'])
def post_devices(request):
    if request.data.get('bulk') is True:
        try:
            # Start timing
            total_start_time = time.time()
            
            # Read data from local CSV file
            with open('data_push/data/devices_large_do_not_use.csv', mode='r') as file:
                reader = csv.DictReader(file)
                data_list = [row for row in reader]

            # Serialize and save data
            serializer = DeviceSerializer(data=data_list, many=True)
            if serializer.is_valid():
                db_start_time = time.time()
                serializer.save()
                total_db_elapsed_time = time.time() - db_start_time
                
                # End timing
                total_elapsed_time = time.time() - total_start_time
                
                return Response(
                    {
                        "message": "Bulk data inserted successfully.",
                        "total_time_taken": f"{total_elapsed_time:.2f} seconds",
                        "total_db_insert_time": f"{total_db_elapsed_time:.2f} seconds",
                    },
                    status=status.HTTP_201_CREATED
                )
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
            {"error": "No data provided"},
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        # Process request data normally
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
