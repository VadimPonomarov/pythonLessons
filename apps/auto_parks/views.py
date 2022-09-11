from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from ..cars.serializers import CarSerializer
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsAdminUser(),
        return super().get_permissions()


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        car = self.request.data
        serializer = self.get_serializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)


class AutoParkById(RetrieveDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
