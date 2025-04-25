from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CarBrand, CarModel, CarPackage, CarListing
from .serializers import CarBrandSerializer, CarModelSerializer, CarPackageSerializer, CarListingSerializer
from django.shortcuts import render


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand']
    search_fields = ['name']

class CarPackageViewSet(viewsets.ModelViewSet):
    queryset = CarPackage.objects.all()
    serializer_class = CarPackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model']

class CarListingViewSet(viewsets.ModelViewSet):
    queryset = CarListing.objects.all()
    serializer_class = CarListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['package', 'year', 'condition']
    search_fields = ['description']

def home_view(request):
    brands = CarBrand.objects.all()
    return render(request, 'cars/home.html', {'brands': brands})