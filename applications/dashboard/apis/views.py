from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdmin
from .. import models
from . import serializers

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAdmin]

    def destroy(self, request, *args, **kwargs):
        request.data.update({'status': False})
        self.partial_update(request, *args, **kwargs)
        return Response(status=204)

class MotherboardViewSet(BaseViewSet):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

class CPUViewSet(BaseViewSet):
    queryset = models.CPU.get_active_objects()
    serializer_class = serializers.CPUSerializer

class RAMViewSet(BaseViewSet):
    queryset = models.RAM.get_active_objects()
    serializer_class = serializers.RAMSerializer

class GPUViewSet(BaseViewSet):
    queryset = models.GPU.get_active_objects()
    serializer_class = serializers.GPUSerializer

class CaseViewSet(BaseViewSet):
    queryset = models.Case.get_active_objects()
    serializer_class = serializers.CaseSerializer

class InternalDrivesViewSet(BaseViewSet):
    queryset = models.InternalDrive.get_active_objects()
    serializer_class = serializers.InternalDriveSerializer

class PowerSupplyViewSet(BaseViewSet):
    queryset = models.PowerSupply.get_active_objects()
    serializer_class = serializers.PowerSupplySerializer