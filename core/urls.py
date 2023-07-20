from django.urls import path
from .views import *
from rest_framework.authtoken import views
from django.contrib.auth import authenticate, login

urlpatterns = [
    path('hello/', index),
    path('signup', CreateUserView.as_view()),
    path('login', LoginApiView.as_view()),
    path('profile', UpdateUserApiView.as_view())
]