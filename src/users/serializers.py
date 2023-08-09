from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from src.users.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, required=True,validators=[
                                     UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(min_length=2, required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, required=True)
    password = serializers.CharField(min_length=2, required=True)
