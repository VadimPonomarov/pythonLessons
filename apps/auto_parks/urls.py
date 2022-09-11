from django.urls import path

from .views import AutoParkListCreateView, AutoParkAddCarView, AutoParkById

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParkById.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]
