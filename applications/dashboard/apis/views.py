from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .. import models
from . import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class MotherboardListView(ListCreateAPIView):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

class SingleMotherboardView(RetrieveUpdateDestroyAPIView):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

    def delete(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.patch(request, *args, **kwargs)
        return Response(status=204)

class CPUViewSet(ModelViewSet):
    queryset = models.CPU.get_active_objects()
    serializer_class = serializers.CPUSerializer

    def destroy(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.partial_update(request, *args, **kwargs)
        return Response(status=204)