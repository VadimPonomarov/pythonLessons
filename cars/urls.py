from django.urls import path
from .views import CarView, CarsView

urlpatterns = [
    path('', CarsView.as_view()),
    path('/car', CarView.as_view()),
    path('/car/<int:pk>', CarView.as_view()),

]
