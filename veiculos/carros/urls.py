from django.urls import path
from .views import CategoryViewSet, VehicleViewSet, PhotoViewSet, VehiclePhotosApiView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('vehicles', VehicleViewSet)
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('vehicles/<int:vehicle_pk>/photos/', VehiclePhotosApiView.as_view(), name='cursos_photos')
]