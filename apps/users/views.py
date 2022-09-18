from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import UserSerializer, AddAvatarSerializer
from rest_framework import status
from .permissions import IsSuperUser

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def get_permission(self):
        if self.request.method == 'GET':
            return IsSuperUser(),
        return super().get_permissions()


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile

class AdminPermissionView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class ActivateUserView(AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)


class DeactivateUserView(AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)


class UserToAdminView(AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)


class AdminToUserView(AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)
