from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import home_view  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('', home_view, name='home'),
    path('api/accounts/', include('accounts.urls')),
]

# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)