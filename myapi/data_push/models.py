from django.db import models

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = 'customers'  # Table name remains 'customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
