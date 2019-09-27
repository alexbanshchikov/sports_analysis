from rest_framework import serializers
from .models import PlayerStatus


class PlayerStatusSerializer(serializers.Serializer):
    class Meta:
        model = PlayerStatus
        fields = ('id', 'name')



    # def create(self, validated_data):
    #     return PlayerStatus.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
