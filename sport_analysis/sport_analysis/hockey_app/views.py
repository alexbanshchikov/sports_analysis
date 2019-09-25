from django.shortcuts import render

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
        name = request.data.get('name')
        serializer = PlayerStatusSerializer(data=name)
        if serializer.is_valid(raise_exception=True):
            names = serializer.save()
        return Response({"success": "names '{}' created successfully".format(names.name)})


# Create your views here.
