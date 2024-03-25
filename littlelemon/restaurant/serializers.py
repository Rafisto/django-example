from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Booking, MenuItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
