from django.contrib.auth import authenticate

from .models import User


class UserService:

    @staticmethod
    def create_user(form):
        return form.save()

    @staticmethod
    def authenticate_user(username, password):
        return authenticate(username=username, password=password)
