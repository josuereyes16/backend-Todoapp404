from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import ProfileCreationSerializer

User = get_user_model()

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileCreationSerializer
