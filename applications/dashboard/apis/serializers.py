from .. import models
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Field
        fields = '__all__'

class FieldReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Field
        fields = ['id', 'name', 'updated_at', 'created_at', 'status']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'

class CPUSocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPUSocket
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producer
        fields = '__all__'

class CaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseType
        fields = '__all__'

class CaseSidePanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseSidePanel
        fields = '__all__'

class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DriveType
        fields = '__all__'

class PowerSupplyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerSupplyType
        fields = '__all__'

class PowerSupplyEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        models = models.PowerSupplyEfficiency
        fields = '__all__'

class RAMTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RAMType
        fields = '__all__'

class GPUSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GPUSeries
        fields = '__all__'

class GPUSyncSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GPUSync
        fields = '__all__'

class ChipsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chipset
        fields = '__all__'

class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Factor
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motherboard
        fields = '__all__'

class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RAM
        fields = '__all__'

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPU
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GPU
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = '__all__'

class InternalDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InternalDrive
        fields = '__all__'

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerSupply
        fields = '__all__'

class CPUFieldSerializer(serializers.ModelSerializer):
    cpu = CPUSerializer(read_only=True)
    class Meta:
        model = models.CPUField
        fields = '__all__'

class RAMFieldSerializer(serializers.ModelSerializer):
    ram = RAMSerializer(read_only=True)
    class Meta:
        model = models.RAMField
        fields = '__all__'

class GPUFieldSerializer(serializers.ModelSerializer):
    gpu = GPUSerializer(read_only=True)
    class Meta:
        model = models.GPUField
        fields = '__all__'