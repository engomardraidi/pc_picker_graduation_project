# Generated by Django 4.2.7 on 2024-01-09 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0117_mobilefield"),
    ]

    operations = [
        migrations.CreateModel(
            name="MobileUse",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "mobile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.mobile",
                    ),
                ),
                (
                    "use",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.mobilefield",
                    ),
                ),
            ],
            options={
                "db_table": "mobile_use",
            },
        ),
    ]
