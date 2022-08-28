from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from cars.serializers import CarSerializer, CarsSerializer
from .models import CarModel


class CarView(APIView):
    def get(self, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        qs = get_object_or_404(CarModel, pk=pk)
        serializer = CarSerializer(qs)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        car = self.request.data
        serializer = CarSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        qs = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(qs, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        qs = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(qs, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        qs = get_object_or_404(CarModel, pk=pk)
        qs.delete()
        return Response('Done')

class CarsView(APIView):
    def get(self, *args, **kwargs):
        qs = CarModel.objects.all()
        serializer = CarsSerializer(qs, many=True)
        return Response(serializer.data)
