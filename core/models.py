from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    SEX = [(MALE, 'Male'), (FEMALE, 'Female')]

    sex = models.CharField(max_length=1, choices=SEX, default=MALE)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField()

class CreateUser(models.Model):
    username = models.CharField(max_length=150,  unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField()
    password_repeat = models.CharField()


class Login(models.Model):
    username = models.CharField(max_length=150,  unique=True)
    password = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UpdatePassword(models.Model):
    old_password = models.CharField()
    new_password = models.CharField()

