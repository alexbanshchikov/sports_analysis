from rest_framework import serializers
from .models import PlayerStatus


class PlayerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatus
        fields = ('id', 'name', )
