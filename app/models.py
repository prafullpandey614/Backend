from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class UserProfile(models.Model):
    # fields like username, email, password, etc.
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    
class Tags(models.Model):
    name = models.CharField(max_length=20)
    

    
class Question(models.Model):
    question = models.TextField()
    tags = models.ManyToManyField(Tags)
    is_solved = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    

class Answers(models.Model):
    question  = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_best = models.BooleanField(default=False)

