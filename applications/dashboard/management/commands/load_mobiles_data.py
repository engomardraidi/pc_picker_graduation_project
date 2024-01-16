from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import Mobile, MobileField, MobileUse
import os

class Command(BaseCommand):
    help = 'Loads data from mobiles.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Mobile.objects.exists():
            print('Mobiles data already loaded...exiting.')
            return

        print("Loading mobiles data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'mobiles.csv')

        for row in DictReader(open(BASE_DIR)):
            mobile = Mobile(
                name=row['Name'],
                price=row['Price'],
                cameras=row['Cameras'],
                cpu=row['CPU'],
                core_count=int(row['Core_count']),
                cpu_speed=float(row['CPU_speed']),
                storage=row['Storage'],
                ram=int(row['Ram']),
                screen_size=float(str(row['Screen_size']).replace(' inches', '')),
                refresh_rate=int(str(row['Refresh_rate']).replace(' Hz', '')),
                battery=int(row['Battery']),
                fast_charging=True if row['Fast_charging'] == 'TRUE' else False,
                main_camera=int(row['Main_camera']),
                front_camera=int(row['Front_camera']),
                cameras_num=int(row['Cameras_num']),
                external_image=row['Image']
            )
            mobile.save(command=True)

            fields = MobileField.get_objects()

            if str(row['Performance_class']).lower() == 'true':
                MobileUse(mobile=mobile, use=fields[0]).save()
            if str(row['Camera_class']).lower() == 'true':
                MobileUse(mobile=mobile, use=fields[1]).save()
            if str(row['Battery_class']).lower() == 'true':
                MobileUse(mobile=mobile, use=fields[2]).save()
            if str(row['Browsing_class']).lower() == 'true':
                MobileUse(mobile=mobile, use=fields[3]).save()