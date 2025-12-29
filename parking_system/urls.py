from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from slots.views import ParkingSlotViewSet
from vehicles.views import VehicleEntryView, VehicleExitView

router = DefaultRouter()
router.register('slots', ParkingSlotViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('vehicles/entry/', VehicleEntryView.as_view()),
    path('vehicles/exit/', VehicleExitView.as_view()),
]
