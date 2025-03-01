from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics
from .serializes import CategorySerializer, VehicleSerializer, PhotosSerializer, VehicleVariationSerializer, LoginSerializer
from .models import Category, Vehicle, Photo, VehicleVariation

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
    
class VehicleVariationViewSet(viewsets.ModelViewSet):
    queryset = VehicleVariation.objects.all()
    serializer_class = VehicleVariationSerializer


class VehicleVehicleVariationsApiView(generics.ListAPIView):
    serializer_class = VehicleVariationSerializer
    
    def get_queryset(self):
        if self.kwargs['vehicle_pk']:
            vehicle_pk = self.kwargs['vehicle_pk']
            return VehicleVariation.objects.filter(vehicle_id=vehicle_pk)
        return self.queryset.all()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"error": "E-mail ou senha inválidos"}, status=400)
            
            if not user.check_password(password):
                return Response({"error": "E-mail ou senha inválidos"}, status=400)

            # Criando o RefreshToken e AccessToken
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)  # Access token com data de expiração
            
            return Response({
                "access_token": access_token,
                "refresh_token": str(refresh),  # Opcional, para poder renovar o token
            })

        return Response({"error": "E-mail ou senha inválidos"}, status=400)