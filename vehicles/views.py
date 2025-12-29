from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Vehicle
from slots.models import ParkingSlot

class VehicleEntryView(APIView):
    def post(self, request):
        slot = ParkingSlot.objects.filter(is_available=True).first()
        if not slot:
            return Response({"error": "No slots available"}, status=400)

        vehicle = Vehicle.objects.create(
            license_plate=request.data['license_plate'],
            slot=slot
        )
        slot.is_available = False
        slot.save()

        return Response({"message": "Vehicle entered"}, status=201)


class VehicleExitView(APIView):
    def post(self, request):
        vehicle = Vehicle.objects.filter(
            license_plate=request.data['license_plate'],
            exit_time__isnull=True
        ).first()

        if not vehicle:
            return Response({"error": "Vehicle not found"}, status=404)

        vehicle.exit_time = timezone.now()
        vehicle.slot.is_available = True
        vehicle.slot.save()
        vehicle.save()

        return Response({"message": "Vehicle exited"})

# Create your views here.
