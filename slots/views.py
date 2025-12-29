from rest_framework import viewsets, permissions
from .models import ParkingSlot
from .serializers import ParkingSlotSerializer


class ParkingSlotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer
    permission_classes = [permissions.IsAdminUser]
