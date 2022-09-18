from rest_framework_simplejwt.tokens import Token, BlacklistMixin

from apps.users.models import UserModel
from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JwtException
from rest_framework.generics import get_object_or_404



class ActivateToken(BlacklistMixin, Token):
    token_type = ActionEnum.ACTIVATE.token_type
    lifetime = ActionEnum.ACTIVATE.exp_time


class jwtService:
    @staticmethod
    def create_token(user):
        return ActivateToken.for_user(user)

    @staticmethod
    def validate_token(token):
        try:
            activate_token = ActivateToken(token)
            activate_token.check_blacklist()
        except (Exception,):
            raise JwtException
        activate_token.blacklist()
        user_id = activate_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)