# views/get_devices.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from data_push.models import Device
from data_push.serializers import DeviceSerializer
from rest_framework import status
import time
from django.db import connection 


@api_view(['GET'])
def get_devices(request):

    start_time = time.time()
    devices = Device.objects.all()
    # devices = Device.objects.exclude(tenant_id=125)

    total_db_elapsed_time = time.time() - start_time
    
    serializer = DeviceSerializer(devices, many=True)
    total_elapsed_time = time.time() - start_time
    return Response(
                    {
                        "message": "Bulk data read successfully.",
                        "total_time_taken": f"{total_elapsed_time} seconds",
                        "total_db_insert_time": f"{total_db_elapsed_time} seconds",
                        "count": len(serializer.data)
                    },
                    status=status.HTTP_201_CREATED
                )


# @api_view(['GET'])
# def get_devices(request):
#     try:
#         start_time = time.time()

#         # Raw SQL query to fetch data where tenant_id != 10000
#         query = "SELECT * FROM devices"
#         with connection.cursor() as cursor:
#             cursor.execute(query)
#             rows = cursor.fetchall()

#         total_db_elapsed_time = time.time() - start_time

#         total_elapsed_time = time.time() - start_time

#         return Response(
#             {
#                 "message": "Bulk data read successfully.",
#                 "total_time_taken": f"{total_elapsed_time:.2f} seconds",
#                 "total_db_read_time": f"{total_db_elapsed_time:.2f} seconds",
#                 "count": len(rows),
#             },
#             status=status.HTTP_200_OK,
#         )

#     except Exception as e:
#         return Response(
#             {"error": f"An unexpected error occurred: {str(e)}"},
#             status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         )
