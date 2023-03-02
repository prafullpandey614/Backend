from dataclasses import field
from operator import mod
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile,Question,Answers
from .validators import validate_email_mobile

class ProfileSerializer(serializers.ModelSerializer):
    email_mobile = serializers.CharField(validators=[validate_email_mobile],write_only=True)
    password = serializers.CharField(write_only=True)
    user_image_url = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['profile_id','username','is_suspended','email_mobile','password','user_image','user_image_url','tagline','private_user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        # extra_kwargs = {'password': {'write_only': True}}
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
        from dataclasses import field
from operator import mod
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile,Question,Answers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
        