from rest_framework import generics,status
from django.contrib.auth.models import User
from  rest_framework.permissions import IsAuthenticated
from .serializer_auth import RegisterSerializer
from app.serializers.serializers import AddQuestionSerializer,AddAnswerSerializer
from .models import Question,Answer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class APIOverview(APIView):
    def get(self, request):
        response = {
            "api" : "app overview",
        }
        return Response(response)
    
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

class UpvoteQuestionView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class= AddQuestionSerializer
    lookup_url_kwarg = 'question_id'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.upvotes+=1
        instance.save()
        return super().update(request, *args, **kwargs)
    
    
class DownvoteQuestionView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class= AddQuestionSerializer
    lookup_url_kwarg = 'question_id'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.downvotes+=1
        instance.save()
        return super().update(request, *args, **kwargs)
    
class AddAnswer(generics.CreateAPIView):
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AddAnswerSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        