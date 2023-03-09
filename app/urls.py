from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
urlpatterns = [
  
    path('', views.APIOverview.as_view(), name='api_over_view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', views.RegistrationView.as_view(), name='token_refresh'),
    path('add-question/', views.AddQuestionView.as_view(), name='add_question'),
    path('upvote-question/<int:question_id>/', views.UpvoteQuestionView.as_view(), name='upvote_question'),
    path('downvote-question/<int:question_id>/', views.DownvoteQuestionView.as_view(), name='downvote_question'),
    path('add-answer/<int:question_id>/', views.UpvoteQuestionView.as_view(), name='upvote_question'),
    
]