from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .permissions import IsAdmin
from .. import models
from . import serializers

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter]
    search_fields = ['name']

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

class LaptopViewSet(BaseViewSet):
    queryset = models.Laptop.get_active_objects()
    serializer_class = serializers.LaptopSerializer

class MobileViewSet(BaseViewSet):
    queryset = models.Mobile.get_active_objects()
    serializer_class = serializers.MobileSerializer

@api_view(['GET'])
@permission_classes([IsAdmin])
def get_all_attributes(request):
    producers = serializers.ProducerSerializer(models.Producer.get_objects(), many=True)
    chipsets = serializers.ChipsetSerializer(models.Chipset.get_objects(), many=True)
    sockets = serializers.CPUSocketSerializer(models.CPUSocket.get_objects(), many=True)
    form_factors = serializers.FormFactorSerializer(models.FormFactor.get_objects(), many=True)
    ram_types = serializers.RAMTypeSerializer(models.RAMType.get_objects(), many=True)
    gpu_syncs = serializers.GPUSyncSerializer(models.GPUSync.get_objects(), many=True)
    gpu_serires = serializers.GPUSeriesSerializer(models.GPUSeries.get_objects(), many=True)
    power_supply_types = serializers.PowerSupplyTypeSerializer(models.PowerSupplyType.get_objects(), many=True)
    power_supply_efficiency = serializers.PowerSupplyEfficiencySerializer(models.PowerSupplyEfficiency.get_objects(), many=True)
    case_types = serializers.CaseTypeSerializer(models.CaseType.get_objects(), many=True)
    case_styles = serializers.CaseStyleSerializer(models.CaseStyle.get_objects(), many=True)
    case_side_panel = serializers.CaseSidePanelSerializer(models.CaseSidePanel.get_objects(), many=True)
    drive_types = serializers.DriveTypeSerializer(models.DriveType.get_objects(), many=True)

    return Response({
        'producers': producers.data,
        'chipsets': chipsets.data,
        'sockets': sockets.data,
        'form_factors': form_factors.data,
        'ram_types': ram_types.data,
        'gpu_syncs': gpu_syncs.data,
        'gpu_serires': gpu_serires.data,
        'power_supply_types': power_supply_types.data,
        'power_supply_efficiency': power_supply_efficiency.data,
        'case_types': case_types.data,
        'case_styles': case_styles.data,
        'case_side_panel': case_side_panel.data,
        'drive_types': drive_types.data,
    })