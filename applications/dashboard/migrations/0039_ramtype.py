# Generated by Django 4.2.7 on 2023-12-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0038_delete_ramtype"),
    ]

    operations = [
        migrations.CreateModel(
            name="RAMType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "ram_type",
            },
        ),
    ]
