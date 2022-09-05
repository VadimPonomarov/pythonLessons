from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
        )
        read_only_field = (
            'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
        )

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
