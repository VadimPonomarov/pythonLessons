from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from core.services.jwt_service import jwtService, RecoverPasswordToken
from core.services.email_service import EmailService
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer, PasswordSerializer
from ..users.models import UserModel


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = jwtService.validate_token(token)
        user.is_active = True
        user.save()
        return Response('Success!!! Done', status=status.HTTP_200_OK)


class RecoverUserPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.data
        serializer = EmailSerializer(data=email)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        user = get_object_or_404(UserModel, email=email)
        EmailService.recover_password_email(user)
        return Response('Success!!! Done', status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        user = jwtService.validate_token(token, RecoverPasswordToken)
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response('Success!!! Done', status=status.HTTP_200_OK)
