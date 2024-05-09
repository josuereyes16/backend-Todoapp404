from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.RESTRICT,
        limit_choices_to={'is_staff': False},
        related_name='tasks',
        null=True
    )
    def _str_(self):
        return self.name
