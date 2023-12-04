from .. import models
from rest_framework import serializers

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Field
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