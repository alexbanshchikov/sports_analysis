from rest_framework import serializers
from .models import PlayerStatus, Amplua, Conference, Division, TimePeriod


class PlayerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatus
        fields = ('id', 'name', )

class AmpluaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amplua
        fields = ('id', 'name')

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('id', 'name')

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('id', 'name')

class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('id', 'name')