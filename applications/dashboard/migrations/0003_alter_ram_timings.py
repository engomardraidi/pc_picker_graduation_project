# Generated by Django 4.2.7 on 2023-11-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_ram"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ram",
            name="timings",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
