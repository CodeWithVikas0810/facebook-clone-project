from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """We have use inherited AbstractUser class and created my own version,
    but in abstract user class email is not unique so we specify a validator in email"""

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
