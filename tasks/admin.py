
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',  'priority', 'user', 'completed',]
    search_fields = ['name', 'description', 'user__username']