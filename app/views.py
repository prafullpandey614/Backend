from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from  rest_framework.permissions import IsAuthenticated
from .serializer_auth import RegisterSerializer
from app.serializers.serializers import AddQuestionSerializer
from .models import Question,Answer
# Create your views here.
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = RegisterSerializer

class AddQuestionView(generics.CreateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AddQuestionSerializer
    
    def perform_create(self, serializer):
        serializer.save(asked_by=self.request.user)
        