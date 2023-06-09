# Generated by Django 4.1.7 on 2023-03-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_project_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="dateF",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, upload_to="static/photos/"),
        ),
    ]
