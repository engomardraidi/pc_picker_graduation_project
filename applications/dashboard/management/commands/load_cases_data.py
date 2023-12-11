from django.db import IntegrityError
from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import Case, Color, CaseType

class Command(BaseCommand):
    help = 'Loads data cases-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Case.objects.exists():
            print('Cases data already loaded...exiting.')
            return

        print("Loading Cases data")

        for row in DictReader(open('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/cases_cleaned.csv')):
            color = None
            if row['color'] != '':
                colors = str(row['color']).split('/')
                color = Color.filter_objects(color=colors[0])
                if len(color) == 0:
                    color = Color(color=colors[0])
                    color.save()
                else:
                    color = color[0]

            
            case_type = CaseType.filter_objects(type=row['type'])
            if len(case_type) == 0:
                case_type = CaseType(type=row['type'])
                case_type.save()
            else:
                case_type = case_type[0]

            case = Case(
                name=row['name'],
                type=case_type,
                color=color,
                price=float(row['price']),
                side_panel=row['side_panel']
            )
            case.save()