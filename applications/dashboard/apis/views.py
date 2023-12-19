from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .. import models
from . import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class MotherboardViewSet(ModelViewSet):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

    def destroy(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.partial_update(request, *args, **kwargs)
        return Response(status=204)

class CPUViewSet(ModelViewSet):
    queryset = models.CPU.get_active_objects()
    serializer_class = serializers.CPUSerializer

    def destroy(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.partial_update(request, *args, **kwargs)
        return Response(status=204)