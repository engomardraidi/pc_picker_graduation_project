from csv import DictReader
from typing import Any
from django.core.management import BaseCommand
from ...models import LaptopField, MobileField, CaseStyle
from ...apis.serializers import PCFieldSerializer

class Command(BaseCommand):
    help = 'Loads fields'

    def handle(self, *args: Any, **options: Any) -> str | None:
      print('Loading fields')

      standard = CaseStyle.objects.get_or_create(style='standard')[0]
      gaming = CaseStyle.objects.get_or_create(style='gaming')[0]

      PC_FIELDS = [
         {
            'name': 'office',
            'cpu_budget': 0.3,
            'gpu_budget': 0.1,
            'motherboard_budget': 0.1,
            'ram_budget': 0.2,
            'having_gpu': 0,
            'case_budget': 0.05,
            'internal_drive_budget': 0.2,
            'power_supply_budget': 0.05,
            'highest_performance': 1,
            'case_style': standard.id
         },
         {
            'name': 'programming',
            'cpu_budget': 0.3,
            'gpu_budget': 0.05,
            'motherboard_budget': 0.15,
            'ram_budget': 0.25,
            'having_gpu': 1,
            'case_budget': 0.05,
            'internal_drive_budget': 0.15,
            'power_supply_budget': 0.05,
            'highest_performance': 2,
            'case_style': standard.id
         },
         {
            'name': 'graphic design',
            'cpu_budget': 0.15,
            'gpu_budget': 0.3,
            'motherboard_budget': 0.1,
            'ram_budget': 0.2,
            'having_gpu': 1,
            'case_budget': 0.05,
            'internal_drive_budget': 0.15,
            'power_supply_budget': 0.05,
            'highest_performance': 3,
            'case_style': gaming.id
         },
         {
            'name': 'gaming',
            'cpu_budget': 0.2,
            'gpu_budget': 0.35,
            'motherboard_budget': 0.1,
            'ram_budget': 0.15,
            'having_gpu': 1,
            'case_budget': 0.05,
            'internal_drive_budget': 0.1,
            'power_supply_budget': 0.05,
            'highest_performance': 4,
            'case_style': gaming.id
         },
      ]
      
      LAPTOP_FIELDS = [
         {
            'name': 'home'
         },
         {
            'name': 'workstation'
         },
         {
            'name': 'gaming'
         }
      ]
      
      MOBILE_FIELDS = [
         {
            'name': 'performance'
         },
         {
            'name': 'camera'
         },
         {
            'name': 'battery'
         },
         {
            'name': 'browsing'
         }
      ]

      for field in PC_FIELDS:
         serializer = PCFieldSerializer(data=field)
         if serializer.is_valid():
            serializer.save()

      for field in LAPTOP_FIELDS:
         LaptopField(name=field['name']).save(command=True)

      for field in MOBILE_FIELDS:
         MobileField(name=field['name']).save(command=True)