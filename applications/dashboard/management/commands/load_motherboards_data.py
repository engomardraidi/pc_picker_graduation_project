from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import Motherboard

class Command(BaseCommand):
    help = 'Loads data from motherboards_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Motherboard.objects.exists():
            print('Motherboard data already loaded...exiting.')
            return

        print("Loading motherboards data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/motherboards_1-cleaned.csv')):
            m2_pci_e_3=int(float(row['m.2 pci-e 3.0']) if row['m.2 pci-e 3.0'].isdigit() else 0)
            m2_pci_e_4=int(float(row['m.2 pci-e 4.0']) if row['m.2 pci-e 4.0'].isdigit() else 0)   
            usb_3_slots=int(float(row['usb 3 slots']) if row['usb 3 slots'].isdigit() else 0)      
            usb_3_headers=int(float(row['usb 3 headers']) if row['usb 3 headers'].isdigit() else 0)
            usb_3_type_c=int(float(row['usb 3 type-c']) if row['usb 3 type-c'].isdigit() else 0)

            motherboard = Motherboard(
                    name=row['name'],
                    from_factor=row['from_factor'],
                    socket=row['socket'],
                    memory_type=row['memory_type'],
                    memory_max_capacity=int(float(row['memory_max_capacity'])),
                    price=float(row['price']),
                    chipset=row['chipset'],
                    producer=row['producer'],
                    ram_slots=int(row['ram_slots']),
                    m2_pci_e_3=m2_pci_e_3,
                    m2_pci_e_4=m2_pci_e_4,
                    usb_3_slots=usb_3_slots,
                    usb_3_headers=usb_3_headers,
                    usb_3_type_c=usb_3_type_c,
                    vga=True if row['vga'] == '1.0' else False,
                    dvi=True if row['dvi'] == '1.0' else False,
                    display_port=True if row['display port'] == '1.0' else False,
                    hdmi=True if row['hdmi'] == '1.0' else False,
                    pci_e_3=int(float(row['pci-e 3.0'])),
                    pci_e_4=int(float(row['pci-e 4.0'])),
                    url=row['url'],
                )
            motherboard.save()