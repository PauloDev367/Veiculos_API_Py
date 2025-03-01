from rest_framework import serializers
from .models import Vehicle, VehicleVariation, Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')