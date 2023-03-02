from django.urls import path
# from .views import UserAPIView,AddQuestionView,SearchQuestionView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import UserCreate
urlpatterns = [
    path("token",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("token/refresh",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("create-user", UserCreate.as_view(),name='create-user'),
    # path("user",UserAPIView.as_view(),name='token_obtain_pair'),
    # path("add-question",AddQuestionView.as_view(),name='add-question'),
    # path("search",SearchQuestionView.as_view(),name='search'),
]
