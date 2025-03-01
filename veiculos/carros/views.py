from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializes import CategorySerializer, VehicleSerializer, PhotosSerializer
from .models import Category, Vehicle, Photo

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotosSerializer


class VehiclePhotosApiView(generics.ListAPIView):
    serializer_class = PhotosSerializer
    
    def get_queryset(self):
        if self.kwargs['vehicle_pk']:
            vehicle_pk = self.kwargs['vehicle_pk']
            return Photo.objects.filter(vehicle_id=vehicle_pk)
        return self.queryset.all()