from django.urls import path

from .views import UserCreateView, ActivateUserView, DeactivateUserView, UserToAdminView, AdminToUserView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/activate', ActivateUserView.as_view()),
    path('/<int:pk>/deactivate', DeactivateUserView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
]
