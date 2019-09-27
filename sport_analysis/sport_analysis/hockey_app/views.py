from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PlayerStatusSerializer
from .models import PlayerStatus


class PlayerStatusView(ListCreateAPIView):
    queryset = PlayerStatus.objects.all()
    serializer_class = PlayerStatusSerializer

    def perform_create(self, serializer):
        player_status = get_object_or_404(PlayerStatus, id=self.request.data.get('id'))
        return serializer.save(player_status=player_status)


class SinglePlayerStatusView(RetrieveUpdateDestroyAPIView):
    queryset = PlayerStatus.objects.all()
    serializer_class = PlayerStatusSerializer
