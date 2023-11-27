from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import RAM

class Command(BaseCommand):
    help = 'Loads data from rams_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if RAM.objects.exists():
            print('RAM data already loaded...exiting.')
            return

        print("Loading RAMs data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/rams_1-cleaned.csv')):
            ram = RAM(
                    name=row['name'],
                    size=int(str(str(row['size']).replace('GB', '')).strip()),
                    memory_type=row['memory_type'],
                    price=float(row['price']),
                    producer=row['producer'],
                    clock=int(row['clock']),
                    timings=row['timings'],
                    sticks=int(row['sticks']),
                    url=row['url'],
                )
            ram.save()