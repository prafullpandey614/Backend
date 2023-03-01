from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username')
        extra_kwargs = {'password': {'write_only': True}}