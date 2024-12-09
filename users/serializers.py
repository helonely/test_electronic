from rest_framework.fields import CharField
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'city', 'password',)


class OtherUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'phone', 'city',)