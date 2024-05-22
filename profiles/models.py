from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    # Añadir otros campos personalizados si es necesario
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profile_set',  # Cambiar 'user_set' a 'profile_set'
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profile_set',  # Cambiar 'user_set' a 'profile_set'
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    password = models.CharField(max_length=128, default='temporary_password')  # Agregar un valor predeterminado
    username = models.CharField(max_length=150, unique=True, default='default_username')  # Agregar un valor predeterminado

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
