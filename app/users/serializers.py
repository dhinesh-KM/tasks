from rest_framework import serializers,status
from .models import User
from django.contrib.auth import hashers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        