from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser

from .models import CarModel
from .serializers import CarAllSerializer, CarSerializer


class CarListView(ListCreateAPIView):
    queryset = CarModel.object.all()
    serializer_class = CarAllSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        auto_park_filter = self.request.query_params.get('auto_park_id')
        if auto_park_filter:
            queryset = super().get_queryset().filter(auto_park=auto_park_filter)
        else:
            queryset = super().get_queryset()
        queryset = queryset.order_by('id')
        return queryset


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.object.all()
    serializer_class = CarSerializer
