from pyexpat import model
from unicodedata import name
import regex as re
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
from .validators import (
    validate_email_mobile
)

class UserManger(BaseUserManager):
    
    def create_user(self,email_mobile,username,password):
        if re.match(r"^\S+@\S+\.\S+$",email_mobile):
            email_mobile = UserManger.normalize_email(email_mobile)
        user = self.model(
            email_mobile = email_mobile,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class UserProfile(AbstractBaseUser):
    # fields like username, email, password, etc.
    profile_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    email_mobile = models.CharField(max_length=255,unique=True,default='',validators=[validate_email_mobile])
    username = models.CharField(max_length=255,unique=True,default='')
    user_image    = models.ImageField(
                                    default='',
                                    upload_to = "images"
                                    )
    tagline       = models.CharField(max_length=2000,default='',blank=True)
    private_user  = models.BooleanField(default=False)  
    is_verified   = models.BooleanField(default=False)     
    password      = models.CharField(max_length=256,default='',editable=False)
    date_joined   = models.DateField(default=timezone.now)
    is_active     = models.BooleanField(default=True) #used by internal team to update the user activation status
    is_suspended  = models.BooleanField(default=False) #used by user her/himself to update the activation status
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    last_login    = models.DateTimeField(auto_now=True,verbose_name='last login')

    USERNAME_FIELD  = 'email_mobile'
    REQUIRED_FIELDS = ['username']
    objects = UserManger()
    
class Tags(models.Model):
    name = models.CharField(max_length=20)
    
class Question(models.Model):
    asked_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True)
    question = models.TextField()
    tags = models.ManyToManyField(Tags,blank=True)
    is_solved = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    

class Answers(models.Model):
    question  = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_best = models.BooleanField(default=False)
    
class NewUserOTP(models.Model):
    email_mobile = models.CharField(max_length=255,unique=True,default='',validators=[validate_email_mobile])
    otp          = models.IntegerField(default=1)
    created_on   = models.DateTimeField(auto_now=True)

class NewModel(models.Model):
    name = models.CharField(max_length=10)
class B3Model(models.Model):
    name= models.CharField(max_length=10)