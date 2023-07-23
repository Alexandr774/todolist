from django.urls import path
from .views import *



urlpatterns = [
    path('hello/', index),
    path('signup', CreateUserView.as_view()),
    path('login', LoginApiView.as_view()),
    path('profile', UpdateUserApiView.as_view()),
    path('update_password', UpdateUserPasswordView.as_view()),
]
