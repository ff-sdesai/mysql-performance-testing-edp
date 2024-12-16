from django.db import models

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)  # Auto-increment primary key
    tenant_id = models.IntegerField()
    device_type = models.CharField(max_length=50)
    column_1 = models.CharField(max_length=255, null=True, blank=True)
    column_2 = models.CharField(max_length=255, null=True, blank=True)
    column_3 = models.CharField(max_length=255, null=True, blank=True)
    column_4 = models.CharField(max_length=255, null=True, blank=True)
    column_5 = models.CharField(max_length=255, null=True, blank=True)
    column_6 = models.CharField(max_length=255, null=True, blank=True)
    column_7 = models.CharField(max_length=255, null=True, blank=True)
    column_8 = models.CharField(max_length=255, null=True, blank=True)
    column_9 = models.CharField(max_length=255, null=True, blank=True)
    column_10 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'devices'  # New table name
