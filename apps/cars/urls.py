from django.urls import path

from .views import CarsView, CarView

urlpatterns = [
    path('', CarsView.as_view()),
    path('/<int:pk>', CarView.as_view())
]
