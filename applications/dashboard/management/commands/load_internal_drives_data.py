from django.db import IntegrityError
from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import InternalDrive, DriveType
import os

class Command(BaseCommand):
    help = 'Loads Internal Drives cases-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if InternalDrive.objects.exists():
            print('Drive data already loaded...exiting.')
            return

        print("Loading Internal Drives data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'internal-drive-cleaned.csv')

        for row in DictReader(open(BASE_DIR)):  
            drive_type = DriveType.objects.get_or_create(type=f'HDD {row["type"]}' if row['type'] != 'SSD' else row['type'])[0]

            internal_drive = InternalDrive(
                name=row['name'],
                price=float(row['price']),
                capacity=int(float(row['capacity'])),
                price_per_gb=float(row['price_per_gb']),
                drive_type=drive_type,
                cache=int(float(row['cache'])),
                form_factor=row['form_factor'],
                interface=row['interface'],
                external_image=row['image_url']
            )
            internal_drive.save(command=True)