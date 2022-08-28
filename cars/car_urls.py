from django.urls import path
from .views import CarView

urlpatterns = [
    path('', CarView.as_view()),
    path('/<int:pk>', CarView.as_view())
]
