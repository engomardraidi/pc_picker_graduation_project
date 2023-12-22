from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Loads data from gpus_1-cleand.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            user = User.objects.get(username='admin')
            print('Super admin is already exist')
        except User.DoesNotExist:
            user = User(username='admin', email='admin@gmail.com', is_superuser=True, is_staff=True)
            user.set_password('adminadmin')
            user.save()
            print('Successfully created')