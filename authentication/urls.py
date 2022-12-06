from .views import  RegisterAPI, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]