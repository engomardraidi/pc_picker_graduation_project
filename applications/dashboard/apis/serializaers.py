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