from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Shipping(models.Model):
    STATUS_CHOICES = (
        ('Dispatched', 'Dispatched'),
        ('Failed Attempt', 'Failed Attempt'),
        ('Delayed', 'Delayed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null = True)
    tracking_number = models.CharField(max_length=500, blank=True, null=True)
    weight_in_kg = models.IntegerField()
    length_in_cm = models.IntegerField()
    height_in_cm = models.IntegerField()
    width_in_cm = models.IntegerField()
    name_of_shipper = models.CharField(max_length=500)
    Recievers_name = models.CharField(max_length=500)
    product = models.CharField(max_length=500)
    Origin = models.CharField(max_length=500)
    Destination = models.CharField(max_length=500)
    Departure_time = models.TimeField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null= True)
    pickup_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)
    lattitude = models.CharField(max_length=500, blank=True, null=True)
    shipment_status = models.CharField(max_length=500, choices=STATUS_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.tracking_number)