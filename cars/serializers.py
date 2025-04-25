from rest_framework import serializers
from .models import CarBrand, CarModel, CarPackage, CarListing

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'logo']

class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'name']

class CarPackageSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(read_only=True)

    class Meta:
        model = CarPackage
        fields = ['id', 'model', 'name', 'battery_capacity']

class CarListingSerializer(serializers.ModelSerializer):
    package = CarPackageSerializer(read_only=True)
    seller = serializers.StringRelatedField()

    class Meta:
        model = CarListing
        fields = [
            'id', 'seller', 'package', 'year', 
            'mileage', 'price', 'condition', 
            'color', 'description', 
            'image1', 'image2', 'image3',
            'listed_at'
        ]