from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.RESTRICT,
        limit_choices_to={'is_superuser': False},
        related_name='tasks',
        null=True
    )
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
    AUTH_USER_MODEL = 'profiles.Profile'
