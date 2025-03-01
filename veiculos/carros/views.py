from django.shortcuts import render
from rest_framework import viewsets
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