# users/serializers.py
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'nickname', 'email', 'avatar',
                  'username', 'password', 'date_joined')