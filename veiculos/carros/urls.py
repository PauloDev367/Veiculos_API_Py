from django.urls import path
from .views import CategoryViewSet, VehicleViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('vehicles', VehicleViewSet)