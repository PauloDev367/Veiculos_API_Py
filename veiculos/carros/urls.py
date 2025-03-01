from django.urls import path
from .views import CategoryViewSet, VehicleViewSet, PhotoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('vehicles', VehicleViewSet)
router.register('photos', PhotoViewSet)