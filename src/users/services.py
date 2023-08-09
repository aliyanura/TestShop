from typing import Tuple
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from src.users.models import User
from src.common.exceptions import ObjectNotFoundException
from src.common.services import Service


class TokenService:
    model = RefreshToken

    @classmethod
    def create_auth_token(cls, username: str, password: str) -> RefreshToken:
        user = authenticate(username=username, password=password)
        if user:
            token = cls.model.for_user(user)
            return token
        else:
            raise ObjectNotFoundException('User not found')


class UserService(Service):
    model = User

    @classmethod
    def create_user(cls, email: str, username: str, password: str,
                    **kwargs) -> User:
        user = cls.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user
