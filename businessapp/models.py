from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    owner_info = models.CharField(max_length=100)
    employee_size = models.IntegerField()
