from django.urls import path
from .views import CategoryViewSet, VehicleViewSet, PhotoViewSet, VehiclePhotosApiView, VehicleVariationViewSet, VehicleVehicleVariationsApiView, LoginView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('vehicles', VehicleViewSet)
router.register('photos', PhotoViewSet)
router.register('vehicle-variations', VehicleVariationViewSet)

urlpatterns = [
    path('vehicles/<int:vehicle_pk>/photos/', VehiclePhotosApiView.as_view(), name='vehicle_photos'),
    path('vehicles/<int:vehicle_pk>/variations/', VehicleVehicleVariationsApiView.as_view(), name='vehicle_variations'),
    path('auth/login/', LoginView.as_view(), name='login'),
]