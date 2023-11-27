# Generated by Django 4.2.7 on 2023-11-26 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0016_alter_pcmotherboard_motherboard_delete_pcparts"),
    ]

    operations = [
        migrations.CreateModel(
            name="PCParts",
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
                    "cpu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.cpu",
                    ),
                ),
                (
                    "gpu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.gpu",
                    ),
                ),
                (
                    "pc_motherboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.pcmotherboard",
                    ),
                ),
                (
                    "ram",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.ram",
                    ),
                ),
            ],
            options={
                "db_table": "pc_parts",
            },
        ),
    ]
