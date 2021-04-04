from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

from users.modelmanager import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        _("email"), max_length=250, unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
