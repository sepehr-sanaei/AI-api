"""
Views for the accounts app.
"""
from rest_framework import generics, permissions, status

from .serializers import UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """
    API view to register a new user.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer
