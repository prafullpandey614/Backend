from django.urls import path
from .views import UserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns = [
    path("token",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("token/refresh",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("user",UserAPIView.as_view(),name='token_obtain_pair'),
]
