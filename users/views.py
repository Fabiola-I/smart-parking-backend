from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ParkingSlot

class ParkingSlotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlot.objects.all()
    permission_classes = [permissions.IsAdminUser]

# Create your views here.
