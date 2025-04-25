# accounts/views.py
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a profile to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner
        return obj.user == request.user

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        """Limit profiles to only the user's own profile"""
        # Update last_active timestamp when user accesses their profile
        profile = UserProfile.objects.get(user=self.request.user)
        profile.last_active = timezone.now()
        profile.save(update_fields=['last_active'])
        
        return UserProfile.objects.filter(user=self.request.user)

class RegisterUserView(generics.CreateAPIView):
    """
    API endpoint for user registration
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        """
        Create a new user and associated profile with required phone number
        """
        # Get data from request
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')
        
        # Validate required fields
        if not username or not email or not password or not phone_number:
            return Response(
                {"error": "Username, email, password and phone number are required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if username or email already exist
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "This username is already taken"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "This email is already registered"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=request.data.get('first_name', ''),
            last_name=request.data.get('last_name', '')
        )
        
        # Update profile with required phone number
        user.profile.phone_number = phone_number
        user.profile.save()
        
        # Return the user data
        serializer = UserProfileSerializer(user.profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)