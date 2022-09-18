from rest_framework.serializers import Serializer, EmailField, ModelSerializer

from apps.users.models import UserModel


class EmailSerializer(Serializer):
    email = EmailField()

class PasswordSerializer(ModelSerializer):
    class Meta:
        model=UserModel
        fields=('password',)