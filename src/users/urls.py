from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from src.users import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view({'post': 'create'}), name='register-user'),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('login/', views.LoginAPIView.as_view({'post': 'create'}), name='login'),
]