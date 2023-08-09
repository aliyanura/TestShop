from django.urls import path
from src.users import views


urlpatterns = [
    path('register', views.RegisterAPIView.as_view({'post': 'create'}), name='register-user'),
    path('login', views.LoginAPIView.as_view({'post': 'create'}), name='login'),
]