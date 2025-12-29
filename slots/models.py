from django.db import models
from django.db import models

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.slot_number

# Create your models here.
