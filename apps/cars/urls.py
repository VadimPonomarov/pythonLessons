from django.urls import path

from .views import CarListView, CarRetrieveUpdateDestroy

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroy.as_view())
]
