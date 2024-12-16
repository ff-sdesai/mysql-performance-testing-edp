# views/get_devices.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from data_push.models import Device
from data_push.serializers import DeviceSerializer

@api_view(['GET'])
def get_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)
