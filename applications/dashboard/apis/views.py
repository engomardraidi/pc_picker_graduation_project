from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .. import models
from . import serializers
from rest_framework.response import Response

class MotherboardListView(ListCreateAPIView):
    queryset = models.Motherboard.filter_objects(status=True)
    serializer_class = serializers.MotherboardSerializer

class SingleMotherboardView(RetrieveUpdateDestroyAPIView):
    queryset = models.Motherboard.filter_objects(status=True)
    serializer_class = serializers.MotherboardSerializer

    def delete(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.patch(request, *args, **kwargs)
        return Response(status=204)