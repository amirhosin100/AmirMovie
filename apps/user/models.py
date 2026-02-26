from django.db import models
from django.contrib.auth.models import AbstractUser

from base.base_model import BaseModel


class User(AbstractUser):
    national_code = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
    )
