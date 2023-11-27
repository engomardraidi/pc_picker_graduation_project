from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import GPU

class Command(BaseCommand):
    help = 'Loads data from gpus_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if GPU.objects.exists():
            print('GPU data already loaded...exiting.')
            return

        print("Loading GPUs data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/gpus_1-cleaned.csv')):
            gpu = GPU(
                    name=row['name'],
                    pci_e=float(row['pci-e']),
                    series=row['series'],
                    vram=int(str(row['vram']).replace('GB', '').strip()),
                    price=float(row['price']),
                    producer=row['producer'],
                    length=float(str(row['length']).replace('mm', '').strip()),
                    slots=float(row['slots']) if row['slots'] != '' else 0.0,
                    connectors_8pin=int(float(row['8-pin connectors'])),
                    connectors_6pin=int(float(row['6-pin connectors'])),
                    hdmi=True if row['hdmi'] == '1.0' else False,
                    display_port=True if row['display port'] == '1.0' else False,
                    dvi=True if row['dvi'] == '1.0' else False,
                    vga=True if row['vga'] == '1.0' else False,
                    boost_clock=int(str(row['boost clock']).replace('MHz', '').strip()),
                    memory_clock=int(str(row['memory clock']).replace('MHz', '').strip()),
                    sync=row['sync'],
                    tdp=int(str(row['tdp']).replace('W', '').strip()),
                    url=row['url'],
                )
            gpu.save()