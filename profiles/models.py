from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    bio = models.TextField(verbose_name="Biography", null=True, blank=True)
