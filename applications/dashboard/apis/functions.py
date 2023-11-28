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