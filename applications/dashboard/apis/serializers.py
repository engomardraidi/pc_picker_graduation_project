from .. import models
from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    pass

class SerializerWithoutImage(BaseSerializer):
    pass

class SerializerWithImage(BaseSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('producer', False):
            data['producer'] = models.Producer.get_object(data['producer']).name
        if data.get('form_factor', False):
            if isinstance(data['form_factor'], int):
                data['form_factor'] = models.FormFactor.get_object(data['form_factor']).form_factor
        if data.get('socket', False):
            data['socket'] = models.CPUSocket.get_object(data['socket']).socket
        if data.get('tdp', False):
            data['tdp'] = f'{data["tdp"]} wattage'

        price = f'{data["price"]}$'
        data.pop('price')
        data['price'] = price

        return data

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
        model = models.PowerSupplyEfficiency
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

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('screen_size', False):
            data['screen_size'] = f'{data["screen_size"]} inch'
        if data.get('cpu_speed', False):
            data['cpu_speed'] = f'{data["cpu_speed"]} GHz'
        if data.get('gpu_speed', False):
            data['gpu_speed'] = f'{data["gpu_speed"]} GHz'
        if data.get('weight', False):
            data['weight'] = f'{data["weight"] / 2.205} kilo'
        if data.get('vram', False):
            data['vram'] = f'{data["vram"]} GB'
        if data.get('memory', False):
            data['memory'] = f'{data["memory"]} GB'

        return data

class MobileSerializer(SerializerWithImage):
    class Meta:
        model = models.Mobile
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('ram', False):
            data['ram'] = f'{data["ram"]} GB'
        if data.get('cpu_speed', False):
            data['cpu_speed'] = f'{data["cpu_speed"]} GHz'
        if data.get('screen_size', False):
            data['screen_size'] = f'{data["screen_size"]} inch'
        if data.get('refresh_rate', False):
            data['refresh_rate'] = f'{data["refresh_rate"]} Hz'
        if data.get('battery', False):
            data['battery'] = f'{data["battery"]} mAh'

        return data

class MotherboardSerializer(SerializerWithImage):
    class Meta:
        model = models.Motherboard
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('memory_max_capacity', False):
            data['memory_max_capacity'] = f'{data["memory_max_capacity"]} GB'
        if data.get('chipset', False):
            data['chipset'] = models.Chipset.get_object(data['chipset']).chipset
        if data.get('ram_type', False):
            data['ram_type'] = models.RAMType.get_object(data['ram_type']).type

        return data

class RAMSerializer(SerializerWithImage):
    class Meta:
        model = models.RAM
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('type', False):
            data['type'] = models.RAMType.get_object(data['type']).type
        if data.get('size', False):
            data['size'] = f'{data["size"]} GB'
        if data.get('clock', False):
            data['clock'] = f'{data["clock"]} GHz'

        return data

class CPUSerializer(SerializerWithImage):
    class Meta:
        model = models.CPU
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('base_clock', False):
            data['base_clock'] = f'{data["base_clock"]} GHz'
        if data.get('turbo_clock', False) or data['turbo_clock'] == 0.0:
            data['turbo_clock'] = f'{data["turbo_clock"]} GHz'

        return data

class GPUSerializer(SerializerWithImage):
    class Meta:
        model = models.GPU
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('series', False):
            data['series'] = models.GPUSeries.get_object(data['series']).series
        if data.get('sync', False):
            data['sync'] = models.GPUSync.get_object(data['sync']).sync
        if data.get('vram', False):
            data['vram'] = f'{data["vram"]} GB'
        if data.get('length', False):
            data['length'] = f'{data["length"]} mm'
        if data.get('boost_clock', False):
            data['boost_clock'] = f'{data["boost_clock"]} GHz'
        if data.get('memory_clock', False):
            data['memory_clock'] = f'{data["memory_clock"]} GHz'

        return data

class CaseSerializer(SerializerWithImage):
    class Meta:
        model = models.Case
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('type', False):
            data['type'] = models.CaseType.get_object(data['type']).type
        if data.get('color', False):
            data['color'] = models.Color.get_object(data['color']).color
        if data.get('side_panel', False):
            data['side_panel'] = models.CaseSidePanel.get_object(data['side_panel']).side_panel
        if data.get('style', False):
            data['style'] = models.CaseStyle.get_object(data['style']).style

        return data

class InternalDriveSerializer(SerializerWithImage):
    class Meta:
        model = models.InternalDrive
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('drive_type', False):
            data['drive_type'] = models.DriveType.get_object(data['drive_type']).type
        if data.get('capacity', False):
            data['capacity'] = f'{data["capacity"]} GB'
        if data.get('price_per_gb', False):
            data['price_per_gb'] = f'{data["price_per_gb"]}$'
        if data.get('cache', False):
            data['cache'] = f'{data["cache"]} MB'

        return data

class PowerSupplySerializer(SerializerWithImage):
    class Meta:
        model = models.PowerSupply
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('type', False):
            data['type'] = models.PowerSupplyType.get_object(data['type']).type
        if data.get('efficiency', False):
            data['efficiency'] = models.PowerSupplyEfficiency.get_object(data['efficiency']).efficiency
        if data.get('wattage', False):
            data['wattage'] = f'{data["wattage"]} wattage'

        return data

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