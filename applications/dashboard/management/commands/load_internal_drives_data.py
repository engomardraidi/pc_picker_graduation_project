from django.db import IntegrityError
from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import InternalDrive, DriveType

class Command(BaseCommand):
    help = 'Loads Internal Drives cases-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if InternalDrive.objects.exists():
            print('Drive data already loaded...exiting.')
            return

        print("Loading Internal Drives data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/internal-drive-cleaned.csv')):  
            drive_type = None
            drive_type = DriveType.filter_objects(type=f'HDD {row["type"]}' if row['type'] != 'SSD' else row['type']) 
            if len(drive_type) == 0:
                drive_type = DriveType(type=f'HDD {row["type"]}' if row['type'] != 'SSD' else row['type'])
                drive_type.save()
            else:
                drive_type = drive_type[0]

            internal_drive = InternalDrive(
                name=row['name'],
                price=float(row['price']),
                capacity=int(float(row['capacity'])),
                price_per_gb=float(row['price_per_gb']),
                drive_type=drive_type,
                cache=int(float(row['cache'])),
                form_factor=row['form_factor'],
                interface=row['interface']
            )
            internal_drive.save()