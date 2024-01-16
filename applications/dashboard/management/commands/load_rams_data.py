from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import RAM, RAMType, Producer, PCField, RAMField
import os

class Command(BaseCommand):
    help = 'Loads data from rams_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if RAM.objects.exists():
            print('RAM data already loaded...exiting.')
            return

        print("Loading RAMs data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'rams_1-cleaned.csv')

        for row in DictReader(open(BASE_DIR)):
            ram_type = RAMType.objects.get_or_create(type=row['memory_type'])[0]
            producer = Producer.objects.get_or_create(name=row['producer'])[0]

            ram = RAM(
                    name=row['name'],
                    size=int(row['size']),
                    type=ram_type,
                    price=float(row['price']),
                    producer=producer,
                    clock=int(row['clock']),
                    timings=row['timings'],
                    sticks=int(row['sticks']),
                    external_image=row['image_url'],
                )
            ram.save(command=True)

            fields = PCField.get_objects()

            if str(row['programming']).lower() == 'true':
                RAMField(ram=ram, field=fields[0]).save()
            if str(row['graphic design']).lower() == 'true':
                RAMField(ram=ram, field=fields[1]).save()
            if str(row['gaming']).lower() == 'true':
                RAMField(ram=ram, field=fields[2]).save()
            if str(row['office']).lower() == 'true':
                RAMField(ram=ram, field=fields[3]).save()