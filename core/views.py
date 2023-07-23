from django.contrib.auth import login, logout
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from core.models import User
from core.serializers import CreateUserSerializer, LoginSerializer, UpdateUserSerializer, UpdateUserPasswordSerializer


def index(request):
    return HttpResponse('hello world')

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer


class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        login(self.request, user=serializer.save())
        return


class UpdateUserApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateUserPasswordView(UpdateAPIView):
    serializer_class = UpdateUserPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


