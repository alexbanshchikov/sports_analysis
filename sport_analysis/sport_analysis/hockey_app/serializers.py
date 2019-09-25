from rest_framework import serializers
from .models import PlayerStatus

class PlayerStatusSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return PlayerStatus.objects.create(**validated_data)