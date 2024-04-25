# serializers.py
from rest_framework import serializers

class PasswordGenerationSerializer(serializers.Serializer):
    length = serializers.IntegerField(default=12, min_value=4, max_value=128)
    uppercase = serializers.BooleanField(default=True)
    lowercase = serializers.BooleanField(default=True)
    digits = serializers.BooleanField(default=True)
    special = serializers.BooleanField(default=True)
