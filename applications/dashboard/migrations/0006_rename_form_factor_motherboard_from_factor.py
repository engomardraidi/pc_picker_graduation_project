# Generated by Django 4.2.7 on 2023-11-25 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_motherboard_alter_cpu_status_alter_ram_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="motherboard",
            old_name="form_factor",
            new_name="from_factor",
        ),
    ]
