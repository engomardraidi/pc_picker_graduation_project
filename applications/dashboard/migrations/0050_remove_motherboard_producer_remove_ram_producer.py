# Generated by Django 4.2.7 on 2023-12-10 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0049_ram_producer_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="motherboard",
            name="producer",
        ),
        migrations.RemoveField(
            model_name="ram",
            name="producer",
        ),
    ]
