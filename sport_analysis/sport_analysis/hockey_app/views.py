from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PlayerStatusSerializer

from .models import PlayerStatus


class PlayerStatusView(APIView):
    def get(self, request):
        name = PlayerStatus.objects.all()
        serializer = PlayerStatusSerializer(name, many=True)
        return Response({"name": serializer.data})

    def post(self, request):
        player_status = request.data.get('player_status')

        serializer = PlayerStatusSerializer(data=player_status)
        if serializer.is_valid(raise_exception=True):
            player_statuses = serializer.save()
        return Response({"success": "names '{}' created successfully".format(player_statuses.name)})

    def put(self, request, pk):
        saved_player_statuses = get_object_or_404(PlayerStatus.objects.all(), pk=pk)
        data = request.data.get('player_status')
        serializer = PlayerStatusSerializer(instance=saved_player_statuses, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            player_status_saved = serializer.save()
        return Response({
            "success": "Player_status '{}' updated successfully".format(player_status_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        player_status = get_object_or_404(PlayerStatus.objects.all(), pk=pk)
        player_status.delete()
        return Response({
            "message": "Player status with id `{}` has been deleted.".format(pk)
        }, status=204)

# Create your views here.
