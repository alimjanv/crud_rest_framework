from rest_framework import serializers
from django.contrib.auth import authenticate

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Foydalanuvchi nomi yoki parol noto‘g‘ri.")
        return user
