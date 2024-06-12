from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "password", "email", "bio"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(ProfileCreationSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.save()
        return instance
