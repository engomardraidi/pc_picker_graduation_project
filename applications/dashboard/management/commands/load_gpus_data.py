from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import GPU, GPUSeries, Producer, GPUSync, PCField, GPUField
import os

class Command(BaseCommand):
    help = 'Loads data from gpus_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if GPU.objects.exists():
            print('GPU data already loaded...exiting.')
            return

        print("Loading GPUs data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'gpus_1-cleaned.csv')

        for row in DictReader(open(BASE_DIR)):
            series = GPUSeries.objects.get_or_create(series=row['series'])[0]
            producer = Producer.objects.get_or_create(name=row['producer'])[0]
            sync = GPUSync.objects.get_or_create(sync=row['sync'])[0]

            gpu = GPU(
                    name=row['name'],
                    pci_e=float(row['pci-e']),
                    series=series,
                    vram=int(row['vram']),
                    cores=int(row['cores']),
                    price=float(row['price']),
                    producer=producer,
                    length=float(row['length']),
                    slots=float(row['slots']) if row['slots'] != '' else 0.0,
                    connectors_8pin=int(float(row['8-pin connectors'])),
                    connectors_6pin=int(float(row['6-pin connectors'])),
                    hdmi=int(float(row['hdmi'])),
                    display_port=int(float(row['display port'])),
                    dvi=int(float(row['dvi'])),
                    vga=int(float(row['vga'])),
                    boost_clock=int(row['boost_clock']),
                    memory_clock=int(row['memory_clock']),
                    sync=sync,
                    tdp=int(row['tdp']),
                    external_image=row['image_url'],
                )
            gpu.save(command=True)

            fields = PCField.get_objects()

            if str(row['programming']).lower() == 'true':
                GPUField(gpu=gpu, field=fields[0]).save()
            if str(row['graphic design']).lower() == 'true':
                GPUField(gpu=gpu, field=fields[1]).save()
            if str(row['gaming']).lower() == 'true':
                GPUField(gpu=gpu, field=fields[2]).save()
            if str(row['office']).lower() == 'true':
                GPUField(gpu=gpu, field=fields[3]).save()