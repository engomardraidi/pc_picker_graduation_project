from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import CPU, CPUSocket, Producer, PCField, CPUField
import os

class Command(BaseCommand):
    help = 'Loads data from cpus_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if CPU.objects.exists():
            print('CPU data already loaded...exiting.')
            return

        print("Loading CPUs data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'cpus_1-cleaned.csv')

        for row in DictReader(open(BASE_DIR)):
            socket = CPUSocket.objects.get_or_create(socket=row['socket'])[0]
            producer = Producer.objects.get_or_create(name=row['producer'])[0]

            cpu = CPU(
                    name=row['name'],
                    socket=socket,
                    price=float(row['price']),
                    producer=producer,
                    base_clock=float(row['base_clock']),
                    turbo_clock=float(row['turbo_clock']),
                    cores=int(row['cores']),
                    threads=int(row['threads']),
                    tdp=int(row['tdp']),
                    integrated_graphics=row['integrated graphics'],
                    external_image=row['image_url'],
                )
            cpu.save(command=True)

            fields = PCField.get_objects()

            if str(row['programming']).lower() == 'true':
                CPUField(cpu=cpu, field=fields[0]).save()
            if str(row['graphic design']).lower() == 'true':
                CPUField(cpu=cpu, field=fields[1]).save()
            if str(row['gaming']).lower() == 'true':
                CPUField(cpu=cpu, field=fields[2]).save()
            if str(row['office']).lower() == 'true':
                CPUField(cpu=cpu, field=fields[3]).save()