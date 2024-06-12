from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileCreationSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileCreationSerializer
    permission_classes = [AllowAny]
