from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializes import CategorySerializer, VehicleSerializer, PhotosSerializer, VehicleVariationSerializer, LoginSerializer
from .models import Category, Vehicle, Photo, VehicleVariation
from .services.authentication import Authenticator

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotosSerializer

class VehiclePhotosApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhotosSerializer
    
    def get_queryset(self):
        if self.kwargs['vehicle_pk']:
            vehicle_pk = self.kwargs['vehicle_pk']
            return Photo.objects.filter(vehicle_id=vehicle_pk)
        return self.queryset.all()
    
class VehicleVariationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = VehicleVariation.objects.all()
    serializer_class = VehicleVariationSerializer


class VehicleVehicleVariationsApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleVariationSerializer
    
    def get_queryset(self):
        if self.kwargs['vehicle_pk']:
            vehicle_pk = self.kwargs['vehicle_pk']
            return VehicleVariation.objects.filter(vehicle_id=vehicle_pk)
        return self.queryset.all()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        auth = Authenticator()
        return auth.authenticate(serializer)