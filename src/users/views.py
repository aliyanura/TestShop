from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from src.users.serializers import RegisterSerializer,\
                                  LoginSerializer
from src.users.services import TokenService, UserService


class RegisterAPIView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.create_user(
            email=serializer.validated_data.get('email'),
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password'),
        )
        return Response(data={
            'message': 'User registered successfully',
            'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = TokenService.create_auth_token(
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password')
        )
        return Response(data={
            'message': 'You have successfully logged in',
            'data': {
                'token': str(token),
                'token_type': 'Token',
            },
            'status': "OK"
        }, status=status.HTTP_200_OK)
