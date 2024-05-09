
# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer

"""""
def index(request):
    tasks = Task.objects.all()
    data = serialize("python", tasks)
    return JsonResponse(data, safe=False)
"""""

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer