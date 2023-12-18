from rest_framework.generics import ListCreateAPIView
from .. import models
from . import serializers

class MotherboardListView(ListCreateAPIView):
    queryset = models.Motherboard.get_objects()
    serializer_class = serializers.MotherboardSerializer