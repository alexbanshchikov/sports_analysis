from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PlayerStatusSerializer
from .models import PlayerStatus


class PlayerStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatusSerializer
    queryset = PlayerStatus.objects.all()
