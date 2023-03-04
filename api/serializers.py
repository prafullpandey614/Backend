from django.contrib.auth import hashers
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

    def __init__(self, *args, **kwargs):
        self.fields["username"].error_messages["required"] = u"Username Required"
        self.fields["username"].error_messages["blank"] = u"Username Required"
        self.fields["email_mobile"].error_messages["required"] = u"Email/Mobile number Required"
        self.fields["email_mobile"].error_messages["blank"] = u"Email/Mobile number Required"
        self.fields["password"].error_messages["required"] = u"Password Required"
        self.fields["password"].error_messages["blank"] = u"Password  Required"
    
    def create(self,validated_data):
        user = UserProfile.objects.create(				
			username = validated_data['username'],
			email_mobile = validated_data['email_mobile'],
			password = hashers.make_password(validated_data['password'])
		)
        return user
    def update(self,instance,validated_data):
        for attr,val in validated_data.items():
            if attr == 'password':
                instance.set_password(val)
            else:
                setattr(instance,attr,val)
        instance.save()
        return instance    
    def get_user_image_url(self,obj):
    	# if obj.is_active and not obj.is_suspended :
        #     return obj.user_image.url
        return '/media/avatar/default_user_image1.jpg'   

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
        from dataclasses import field

from rest_framework import serializers
from .models import UserProfile,Question,Answers

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
        