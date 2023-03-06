from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer_auth import RegisterSerializer
# Create your views here.
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = RegisterSerializer