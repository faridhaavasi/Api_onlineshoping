from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password']


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField(write_only=True)
