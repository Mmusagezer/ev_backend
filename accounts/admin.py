# accounts/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'is_phone_verified', 'joined_date', 'last_active']
    search_fields = ['user__username', 'user__email', 'phone_number']
    list_filter = ['is_phone_verified']
    readonly_fields = ['joined_date', 'last_active']