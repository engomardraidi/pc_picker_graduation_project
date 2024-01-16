from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import Motherboard, CPUSocket, FormFactor, RAMType, Chipset, Producer

class Command(BaseCommand):
    help = 'Loads data from motherboards_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Motherboard.objects.exists():
            print('Motherboard data already loaded...exiting.')
            return

        print("Loading motherboards data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/motherboards_1-cleaned.csv')):
            socket = CPUSocket.objects.get_or_create(socket=row['socket'])[0]
            form_factor = FormFactor.objects.get_or_create(form_factor=row['from_factor'])[0]
            ram_type = RAMType.objects.get_or_create(type=row['memory_type'])[0]
            chipset = Chipset.objects.get_or_create(chipset=row['chipset'])[0]
            producer = Producer.objects.get_or_create(name=row['producer'])[0]

            m2_pci_e_3=int(float(row['m.2 pci-e 3.0']) if row['m.2 pci-e 3.0'].isdigit() else 0)
            m2_pci_e_4=int(float(row['m.2 pci-e 4.0']) if row['m.2 pci-e 4.0'].isdigit() else 0)   
            usb_3_slots=int(float(row['usb 3 slots']) if row['usb 3 slots'].isdigit() else 0)      
            usb_3_headers=int(float(row['usb 3 headers']) if row['usb 3 headers'].isdigit() else 0)
            usb_3_type_c=int(float(row['usb 3 type-c']) if row['usb 3 type-c'].isdigit() else 0)

            motherboard = Motherboard(
                    name=row['name'],
                    form_factor=form_factor,
                    socket=socket,
                    ram_type=ram_type,
                    memory_max_capacity=int(float(row['memory_max_capacity'])),
                    price=float(row['price']),
                    chipset=chipset,
                    producer=producer,
                    ram_slots=int(row['ram_slots']),
                    m2_pci_e_3=m2_pci_e_3,
                    m2_pci_e_4=m2_pci_e_4,
                    usb_3_slots=usb_3_slots,
                    usb_3_headers=usb_3_headers,
                    usb_3_type_c=usb_3_type_c,
                    vga=0.0 if row['vga'] == '' else int(float(row['vga'])),
                    dvi=0.0 if row['dvi'] == '' else int(float(row['dvi'])),
                    display_port=0.0 if row['display port'] == '' else int(float(row['display port'])),
                    hdmi=0.0 if row['hdmi'] == '' else int(float(row['hdmi'])),
                    pci_e_3=int(float(row['pci-e 3.0'])),
                    pci_e_4=int(float(row['pci-e 4.0'])),
                    external_image=row['external_image'],
                )
            motherboard.save(command=True)