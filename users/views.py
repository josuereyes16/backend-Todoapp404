# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize



from .models import User

def index(request):
    users = User.objects.all()
    data = serialize("python", users)
    return JsonResponse(data, safe=False)