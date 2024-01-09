from .. import models
from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    pass

class SerializerWithoutImage(BaseSerializer):
    pass

class SerializerWithImage(BaseSerializer):
    def validate(self, attrs):
        if not self.partial:
            external_image = attrs.get('external_image', None)
            image = attrs.get('image', None)
    
            if external_image is None and image is None:
                raise serializers.ValidationError({'image': 'Please upload an image or enter external image url.'})

        return super().validate(attrs)

class DeviceSerializer(SerializerWithoutImage):
    class Meta:
        model = models.Device
        fields = '__all__'

class LaptopFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.LaptopField
        fields = '__all__'

class MobileFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.MobileField
        fields = '__all__'

class PCFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.PCField
        fields = '__all__'

class PCFieldReadSerializer(SerializerWithoutImage):
    class Meta:
        model = models.PCField
        fields = ['id', 'name', 'updated_at', 'created_at', 'status']

class ColorSerializer(SerializerWithoutImage):
    class Meta:
        model = models.Color
        fields = '__all__'

class CPUSocketSerializer(SerializerWithoutImage):
    class Meta:
        model = models.CPUSocket
        fields = '__all__'

class ProducerSerializer(SerializerWithoutImage):
    class Meta:
        model = models.Producer
        fields = '__all__'

class CaseTypeSerializer(SerializerWithoutImage):
    class Meta:
        model = models.CaseType
        fields = '__all__'

class CaseStyleSerializer(SerializerWithoutImage):
    class Meta:
        model = models.CaseStyle
        fields = '__all__'

class CaseSidePanelSerializer(SerializerWithoutImage):
    class Meta:
        model = models.CaseSidePanel
        fields = '__all__'

class DriveTypeSerializer(SerializerWithoutImage):
    class Meta:
        model = models.DriveType
        fields = '__all__'

class PowerSupplyTypeSerializer(SerializerWithoutImage):
    class Meta:
        model = models.PowerSupplyType
        fields = '__all__'

class PowerSupplyEfficiencySerializer(SerializerWithoutImage):
    class Meta:
        models = models.PowerSupplyEfficiency
        fields = '__all__'

class RAMTypeSerializer(SerializerWithoutImage):
    class Meta:
        model = models.RAMType
        fields = '__all__'

class GPUSeriesSerializer(SerializerWithoutImage):
    class Meta:
        model = models.GPUSeries
        fields = '__all__'

class GPUSyncSerializer(SerializerWithoutImage):
    class Meta:
        model = models.GPUSync
        fields = '__all__'

class ChipsetSerializer(SerializerWithoutImage):
    class Meta:
        model = models.Chipset
        fields = '__all__'

class FormFactorSerializer(SerializerWithoutImage):
    class Meta:
        model = models.FormFactor
        fields = '__all__'

class LaptopSerializer(SerializerWithImage):
    class Meta:
        model = models.Laptop
        fields = '__all__'

class MobileSerializer(SerializerWithImage):
    class Meta:
        model = models.Mobile
        fields = '__all__'

class MotherboardSerializer(SerializerWithImage):
    class Meta:
        model = models.Motherboard
        fields = '__all__'

class RAMSerializer(SerializerWithImage):
    class Meta:
        model = models.RAM
        fields = '__all__'

class CPUSerializer(SerializerWithImage):
    class Meta:
        model = models.CPU
        fields = '__all__'

class GPUSerializer(SerializerWithImage):
    class Meta:
        model = models.GPU
        fields = '__all__'

class CaseSerializer(SerializerWithImage):
    class Meta:
        model = models.Case
        fields = '__all__'

class InternalDriveSerializer(SerializerWithImage):
    class Meta:
        model = models.InternalDrive
        fields = '__all__'

class PowerSupplySerializer(SerializerWithImage):
    class Meta:
        model = models.PowerSupply
        fields = '__all__'

class CPUFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.CPUField
        fields = '__all__'

class RAMFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.RAMField
        fields = '__all__'

class GPUFieldSerializer(SerializerWithoutImage):
    class Meta:
        model = models.GPUField
        fields = '__all__'

class LaptopUseSerializer(SerializerWithoutImage):
    class Meta:
        model = models.LaptopUse
        fields = '__all__'

class MobileUseSerializer(SerializerWithoutImage):
    class Meta:
        model = models.MobileUse
        fields = '__all__'