from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Vehicle(Base):
    mileage = models.FloatField()
    year = models.IntegerField()
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='main-photos/')
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class Photo(Base):
    path = models.ImageField()
    vehicle = models.ForeignKey(Vehicle, related_name='vehicles_photos', on_delete=models.SET_NULL, blank=True, null=True)
    
class VehicleVariation(Base):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField()
    color = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicles', on_delete=models.SET_NULL, blank=True, null=True)