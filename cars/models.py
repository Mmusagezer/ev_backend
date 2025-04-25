from django.db import models
from django.contrib.auth.models import User

class CarBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brand_logos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.brand.name} {self.name}"

class CarPackage(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='packages')
    name = models.CharField(max_length=100)  # e.g., "Long Range", "Performance"
    battery_capacity = models.FloatField(help_text="Battery capacity in kWh")
    
    def __str__(self):
        return f"{self.model} - {self.name}"

class CarListing(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair')
    ]
    
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(CarPackage, on_delete=models.CASCADE)
    
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    
    # Optional details
    color = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    # Image uploads
    image1 = models.ImageField(upload_to='car_listings/', null=True)
    image2 = models.ImageField(upload_to='car_listings/', null=True, blank=True)
    image3 = models.ImageField(upload_to='car_listings/', null=True, blank=True)
    
    # Timestamps
    listed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.package} - {self.year} - ${self.price}"