# Generated by Django 4.1.7 on 2023-03-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
        ("portfolio", "0003_alter_project_datef_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.ManyToManyField(blank=True, to="services.service"),
        ),
    ]
