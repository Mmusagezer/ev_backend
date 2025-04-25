from django.contrib import admin
from .models import CarBrand, CarModel, CarPackage, CarListing

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarPackage)
admin.site.register(CarListing)