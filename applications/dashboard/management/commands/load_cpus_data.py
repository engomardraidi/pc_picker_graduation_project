from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import CPU

class Command(BaseCommand):
    help = 'Loads data from cpus_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if CPU.objects.exists():
            print('CPU data already loaded...exiting.')
            return

        print("Loading CPUs data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/cpus_1-cleaned.csv')):
            cpu = CPU(
                    name=row['name'],
                    socket=row['socket'],
                    price=float(row['price']),
                    producer=row['producer'],
                    base_clock=float(str(row['base clock']).replace(' ', '').replace('GHz', '0').strip()),
                    turbo_clock=float(str(row['turbo clock']).replace(' ', '').replace('GHz', '0').strip()),
                    cores=int(row['cores']),
                    threads=int(row['threads']),
                    tdp=int(str(row['tdp']).replace('W', '').strip()),
                    integrated_graphics=row['integrated graphics'],
                    url=row['url'],
                )
            cpu.save()