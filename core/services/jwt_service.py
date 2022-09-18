from typing import Type

from rest_framework_simplejwt.tokens import Token, BlacklistMixin

from apps.users.models import UserModel
from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JwtException
from rest_framework.generics import get_object_or_404


class ActivateToken(BlacklistMixin, Token):
    token_type = ActionEnum.ACTIVATE.token_type
    lifetime = ActionEnum.ACTIVATE.exp_time


class RecoverPasswordToken(BlacklistMixin, Token):
    token_type = ActionEnum.RECOVER_PASSWORD.token_type
    lifetime = ActionEnum.RECOVER_PASSWORD.exp_time


class jwtService:
    @staticmethod
    def create_token(user, token_class: Type[BlacklistMixin | Token]):
        return ActivateToken.for_user(user)

    @staticmethod
    def create_recover_password_token(user, token_class: Type[BlacklistMixin | Token]):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: Type[BlacklistMixin | Token]):
        try:
            action_with_token = token_class(token)
            action_with_token.check_blacklist()
        except (Exception,):
            raise JwtException
        action_with_token.blacklist()
        user_id = action_with_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)

