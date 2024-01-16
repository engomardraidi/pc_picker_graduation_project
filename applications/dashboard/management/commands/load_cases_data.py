from django.db import IntegrityError
from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from django.conf import settings
from ...models import Case, Color, CaseType, CaseSidePanel, CaseStyle
import os

class Command(BaseCommand):
    help = 'Loads data cases-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if Case.objects.exists():
            print('Cases data already loaded...exiting.')
            return

        print("Loading Cases data")

        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets', 'cases_cleaned.csv')

        for row in DictReader(open(BASE_DIR)):
            color = Color.objects.get_or_create(color=row['color'])[0]
            case_type = CaseType.objects.get_or_create(type=row['type'])[0]
            side_panel = CaseSidePanel.objects.get_or_create(side_panel=row['side_panel'])[0]
            style = CaseStyle.objects.get_or_create(style=row['style'])[0]

            case = Case(
                name=row['name'],
                type=case_type,
                color=color,
                price=float(row['price']),
                side_panel=side_panel,
                style=style,
                external_image=row['image_url']
            )
            case.save(command=True)