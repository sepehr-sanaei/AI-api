"""
serializers for the accounts app.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for User sing up.
    """
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def validate(self, data):
        """Validate that both passwords match."""
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """Create and return a new user."""
        password = validated_data.pop('password1')
        email = validated_data.pop('email')
        user = User.objects.create_user(email=email, password=password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update and return an existing user."""
        password = validated_data.pop('password1', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user