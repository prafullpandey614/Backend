from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,blank=True)
    dp = models.ImageField(upload_to="uploads/images/",blank= True)
    score = models.IntegerField(default=0)

class Question(models.Model):
    question = models.TextField()
    img_desc = models.ImageField(upload_to="uploads/images/",blank=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    best_answer_found = models.BooleanField(default=False)
    reports = models.IntegerField(default=0)
    def __str__(self):
        strng = self.question[:15]
        return f"{strng} {self.asked_by}"
    
class Answer(models.Model):
    ans = models.TextField()
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)