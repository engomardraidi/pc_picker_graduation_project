from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .. import models
from . import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class BaseViewSet(ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.partial_update(request, *args, **kwargs)
        return Response(status=204)

class MotherboardViewSet(BaseViewSet):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

class CPUViewSet(BaseViewSet):
    queryset = models.CPU.get_objects()
    serializer_class = serializers.CPUSerializer