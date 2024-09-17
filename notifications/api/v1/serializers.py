from rest_framework import serializers
from ...models import Device
from django.contrib.auth.models import User

class FcmTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('fcm_token','device_name')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password')