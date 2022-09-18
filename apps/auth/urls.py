from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView, RecoverUserPasswordView, ChangePasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recover', RecoverUserPasswordView.as_view()),
    path('/recover/<str:token>', ChangePasswordView.as_view()),

]
