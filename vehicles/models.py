from django.db import models
from django.db import models
from slots.models import ParkingSlot

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_plate

# Create your models here.
