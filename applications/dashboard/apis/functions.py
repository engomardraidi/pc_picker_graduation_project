from .. import models
from . import serializers

def classification_cpu():
    programming = models.Field.get_object(1)
    graphic_design = models.Field.get_object(2)
    cpus = models.CPU.get_objects()

    for cpu in cpus:
        new_data = []
        if cpu.cores >= 4 and cpu.base_clock > 2:
            new_data.append(models.CPUField(cpu=cpu, field=programming).to_json())
            new_data.append(models.CPUField(cpu=cpu, field=graphic_design).to_json())
            serializer = serializers.CPUFieldSerializer(data=new_data, many=True)
            if serializer.is_valid():
                serializer.save()
        elif cpu.cores >= 4 and cpu.base_clock >= 2:
            serializer = serializers.CPUFieldSerializer(data=models.CPUField(cpu=cpu, field=programming).to_json())
            if serializer.is_valid():
                serializer.save()

def classification_ram():
    programming = models.Field.get_object(1)
    graphic_design = models.Field.get_object(2)
    rams = models.RAM.get_objects()

    for ram in rams:
        new_data = []
        if ram.size >= 16:
            new_data.append(models.RAMField(ram=ram, field=programming).to_json())
            new_data.append(models.RAMField(ram=ram, field=graphic_design).to_json())
            serializer = serializers.RAMFieldSerializer(data=new_data, many=True)
            if serializer.is_valid():
                serializer.save()
        elif ram.size >= 8:
            serializer = serializers.RAMFieldSerializer(data=models.RAMField(ram=ram, field=programming).to_json())
            if serializer.is_valid():
                serializer.save()

def classification_gpu():
    programming = models.Field.get_object(1)
    graphic_design = models.Field.get_object(2)
    gpus = models.GPU.get_objects()

    for gpu in gpus:
        new_data = []
        if gpu.vram >= 2:
            new_data.append(models.GPUField(gpu=gpu, field=programming).to_json())
            new_data.append(models.GPUField(gpu=gpu, field=graphic_design).to_json())
            serializer = serializers.GPUFieldSerializer(data=new_data, many=True)
            if serializer.is_valid():
                serializer.save()
        else:
            serializer = serializers.GPUFieldSerializer(data=models.GPUField(gpu=gpu, field=programming).to_json())
            if serializer.is_valid():
                serializer.save()