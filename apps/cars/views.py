from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.serializers import CarSerializer, CarsSerializer

from .models import CarModel
from .services import set_filter


class CarView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarsView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return set_filter(queryset, self.request)
