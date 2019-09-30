from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PlayerStatusSerializer, AmpluaSerializer, ConferenceSerializer, DivisionSerializer, TimePeriodSerializer
from .models import PlayerStatus, Amplua, Conference, Division, TimePeriod


class PlayerStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatusSerializer
    queryset = PlayerStatus.objects.all()


class AmpluaViewSet(viewsets.ModelViewSet):
    serializer_class = AmpluaSerializer
    queryset = Amplua.objects.all()

class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()

class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()

class TimePeriodViewSet(viewsets.ModelViewSet):
    serializer_class = TimePeriodSerializer
    queryset = TimePeriod.objects.all()