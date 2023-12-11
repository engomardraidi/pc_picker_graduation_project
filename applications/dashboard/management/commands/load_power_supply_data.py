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
            power_type = PowerSupplyType.filter_objects(type=row['type'])
            if len(power_type) == 0:
                power_type = PowerSupplyType(type=row['type'])
                power_type.save()
            else:
                power_type = power_type[0]

            
            power_efficiency = PowerSupplyEfficiency.filter_objects(efficiency=row['efficiency'])
            if len(power_efficiency) == 0:
                power_efficiency = PowerSupplyEfficiency(efficiency=row['efficiency'])
                power_efficiency.save()
            else:
                power_efficiency = power_efficiency[0]

            power_supply = PowerSupply(
                name=row['name'],
                price=float(row['price']),
                type=power_type,
                efficiency=power_efficiency,
                wattage=row['wattage']
            )
            power_supply.save()