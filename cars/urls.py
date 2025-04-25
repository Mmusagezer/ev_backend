from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarBrandViewSet, CarModelViewSet, CarPackageViewSet, CarListingViewSet

router = DefaultRouter()
router.register(r'brands', CarBrandViewSet)
router.register(r'models', CarModelViewSet)
router.register(r'packages', CarPackageViewSet)
router.register(r'listings', CarListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]