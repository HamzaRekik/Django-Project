# Generated by Django 4.1.7 on 2023-03-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Logo Design", "Logo Design"),
                            ("Web Design", "Web Design"),
                            ("Video Production", "Video Production"),
                            ("Animation", "Animation"),
                            ("3D Modeling", "3D Modeling"),
                        ],
                        default="Web Design",
                        max_length=50,
                    ),
                ),
                ("description", models.TextField(default="Empty")),
            ],
        ),
    ]
