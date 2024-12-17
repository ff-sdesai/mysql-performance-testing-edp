# views/post_devices.py
import csv
import time
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from data_push.models import Device
from data_push.serializers import DeviceSerializer
from django.db import connection


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

            # Prepare data for bulk_create
            devices = [
                Device(
                    tenant_id=row['tenant_id'],
                    device_type=row['device_type'],
                    column_1=row['column_1'],
                    column_2=row['column_2'],
                    column_3=row['column_3'],
                    column_4=row['column_4'],
                    column_5=row['column_5'],
                    column_6=row['column_6'],
                    column_7=row['column_7'],
                    column_8=row['column_8'],
                    column_9=row['column_9'],
                    column_10=row['column_10']
                )
                for row in data_list
            ]

            # Bulk insert using bulk_create
            db_start_time = time.time()
            Device.objects.bulk_create(devices, batch_size=10000)  # Batch size based on requirements
            total_db_elapsed_time = time.time() - db_start_time

            # End timing
            total_elapsed_time = time.time() - total_start_time

            return Response(
                {
                    "message": "Bulk data inserted successfully.",
                    "total_time_taken": f"{total_elapsed_time:.2f} seconds",
                    "total_db_insert_time": f"{total_db_elapsed_time:.2f} seconds",
                    "total_records_inserted": len(devices),
                },
                status=status.HTTP_201_CREATED
            )

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



# @api_view(['POST'])
# def post_devices(request):
#     if request.data.get('bulk') is True:
#         try:
#             # Start timing
#             total_start_time = time.time()
            
#             # Read data from local CSV file
#             with open('data_push/data/devices_large_do_not_use.csv', mode='r') as file:
#                 reader = csv.DictReader(file)
#                 data_list = [row for row in reader]
            
#             # Prepare bulk insert data
#             values = [
#                 (
#                     row['tenant_id'], row['device_type'],
#                     row['column_1'], row['column_2'], row['column_3'],
#                     row['column_4'], row['column_5'], row['column_6'],
#                     row['column_7'], row['column_8'], row['column_9'], row['column_10']
#                 )
#                 for row in data_list
#             ]

#             # Construct bulk INSERT query
#             db_start_time = time.time()
#             with connection.cursor() as cursor:
#                 query = """
#                 INSERT INTO devices (tenant_id, device_type, column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8, column_9, column_10)
#                 VALUES {}
#                 """.format(
#                     ",".join(["( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"] * len(values))
#                 )
#                 # Flatten values for cursor execution
#                 flat_values = [item for sublist in values for item in sublist]
#                 cursor.execute(query, flat_values)

#             total_db_elapsed_time = time.time() - db_start_time

#             # End timing
#             total_elapsed_time = time.time() - total_start_time

#             return Response(
#                 {
#                     "message": "Bulk data inserted successfully.",
#                     "total_time_taken": f"{total_elapsed_time:.2f} seconds",
#                     "total_db_insert_time": f"{total_db_elapsed_time:.2f} seconds",
#                 },
#                 status=status.HTTP_201_CREATED
#             )

#         except FileNotFoundError:
#             return Response(
#                 {"error": "Local file data.csv not found."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         except Exception as e:
#             return Response(
#                 {"error": f"An unexpected error occurred: {str(e)}"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

#     elif not request.data:  # Handle empty request data
#         return Response(
#             {"error": "No data provided"},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     else:
#         # Process request data normally
#         data = request.data
#         try:
#             db_start_time = time.time()
#             with connection.cursor() as cursor:
#                 query = """
#                 INSERT INTO devices (tenant_id, device_type, column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8, column_9, column_10)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                 """
#                 cursor.execute(
#                     query,
#                     [
#                         data['tenant_id'], data['device_type'],
#                         data['column_1'], data['column_2'], data['column_3'],
#                         data['column_4'], data['column_5'], data['column_6'],
#                         data['column_7'], data['column_8'], data['column_9'], data['column_10']
#                     ]
#                 )
#             total_db_elapsed_time = time.time() - db_start_time

#             return Response(
#                 {"message": "Data inserted successfully.", "total_db_insert_time": f"{total_db_elapsed_time:.2f} seconds"},
#                 status=status.HTTP_201_CREATED
#             )
#         except Exception as e:
#             return Response(
#                 {"error": f"An unexpected error occurred: {str(e)}"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
