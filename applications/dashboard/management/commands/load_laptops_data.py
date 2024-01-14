from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import Laptop, LaptopField, LaptopUse

class Command(BaseCommand):
    help = 'Loads data from laptops-ready.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Laptop.objects.exists():
            print('Laptops data already loaded...exiting.')
            return

        print("Loading Laptops data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/laptops-readiest.csv')):
            laptop = Laptop(
                name=row['Name'],
                screen_size=float(row['Screen_Size']),
                cpu_type=row['CPU_type'],
                memory=int(row['Memory']),
                storage=row['Storage'],
                gpu=row['GPU'],
                vram=round(float(row['VRAM'])),
                gpu_speed=float(row['GPU_Speed']),
                gpu_cores=int(row['GPU_Cores']),
                resolution=row['Resolution'],
                weight=float(row['Weight']),
                backlit_keyboard=True if row['Backlit_Keyboard'].find('N') == -1 else False,
                touchscreen=True if row['Touchscreen'] == 'Yes' else False,
                cpu_speed=float(row['CPU_Speed']),
                number_of_cores=row['Number_of_Cores'],
                display_type=row['Display_Type'],
                graphic_type=row['Graphic_Type'],
                operating_system=row['Operating_System'],
                webcam=True if row['Webcam'] == 'Yes' else False,
                price=row['Price'],
                external_image=row['Image']
            )
            laptop.save(command=True)

            fields = LaptopField.get_objects()

            if str(row['Home']).lower() == 'true':
                LaptopUse(laptop=laptop, use=fields[0]).save()
            if str(row['Workstation']).lower() == 'true':
                LaptopUse(laptop=laptop, use=fields[1]).save()
            if str(row['Gaming']).lower() == 'true':
                LaptopUse(laptop=laptop, use=fields[2]).save()