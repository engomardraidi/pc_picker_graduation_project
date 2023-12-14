from .. import models
from . import serializers

def get_None_or_JSON(instance):
    return None if instance == None else instance.to_json()

def get_total_price(pc):
    total_price = 0
    total_price += 0 if pc.motherboard == None else pc.motherboard.price
    total_price += 0 if pc.cpu == None else pc.cpu.price
    total_price += 0 if pc.ram == None else pc.ram.price
    total_price += 0 if pc.gpu == None else pc.gpu.price
    total_price += 0 if pc.case_part == None else pc.case_part.price
    total_price += 0 if pc.internal_drive == None else pc.internal_drive.price
    total_price += 0 if pc.power_supply == None else pc.power_supply.price

    return total_price

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