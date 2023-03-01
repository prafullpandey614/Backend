from django.shortcuts import render

from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user