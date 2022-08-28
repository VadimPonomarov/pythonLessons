from django.urls import path
from .views import CarsView

urlpatterns = [
    path('', CarsView.as_view()),
]