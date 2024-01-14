from django.db import IntegrityError
from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import PowerSupply, PowerSupplyType, PowerSupplyEfficiency

class Command(BaseCommand):
    help = 'Loads data power-supply-cleaned.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if PowerSupply.objects.exists():
            print('Power supply data already loaded...exiting.')
            return

        print("Loading power supply data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/power-supply-cleaned.csv')):
            power_type = PowerSupplyType.objects.get_or_create(type=row['type'])[0]
            power_efficiency = PowerSupplyEfficiency.objects.get_or_create(efficiency=row['efficiency'])[0]

            power_supply = PowerSupply(
                name=row['name'],
                price=float(row['price']),
                type=power_type,
                efficiency=power_efficiency,
                wattage=row['wattage'],
                external_image=row['image_url']
            )
            power_supply.save(command=True)