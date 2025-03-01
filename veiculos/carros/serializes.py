from rest_framework import serializers
from .models import Vehicle, VehicleVariation, Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'mileage',
            'year',
            'name',
            'main_photo',
            'color',
            'fuel_type',
            'category',
            'price',
        )

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'id',
            'path',
            'vehicle',
        )


class VehicleVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleVariation
        fields = (
            'id',
            'name',
            'main_photo',
            'color',
            'vehicle',
        )
