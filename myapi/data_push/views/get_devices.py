# views/get_devices.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from data_push.models import Device
from data_push.serializers import DeviceSerializer
from rest_framework import status
import time


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
