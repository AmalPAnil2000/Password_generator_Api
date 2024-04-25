# serializers.py
from rest_framework import serializers

class PasswordGenerationOptionsSerializer(serializers.Serializer):
    uppercase = serializers.BooleanField(default=True)
    lowercase = serializers.BooleanField(default=True)
    digits = serializers.BooleanField(default=True)
    special = serializers.BooleanField(default=True)
