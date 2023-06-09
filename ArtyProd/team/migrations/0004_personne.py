# Generated by Django 4.1.7 on 2023-03-25 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personne",
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
                ("name", models.CharField(max_length=50)),
                ("file_cv", models.FileField(blank=True, upload_to="static/cv/")),
                (
                    "post",
                    models.CharField(
                        choices=[
                            ("Graphic Designer", "Graphic Designer"),
                            ("Web Designer", "Web Designer"),
                            ("UI/UX Designer", "UI/UX Designer"),
                            ("Creative Director", "Creative Director"),
                            ("Art Director", "Art Director"),
                            ("Copywriter", "Copywriter"),
                            ("Social Media Manager", "Social Media Manager"),
                            ("Marketing Manager", "Marketing Manager"),
                            ("Project Manager", "Project Manager"),
                            ("Account Manager", "Account Manager"),
                            ("Production Manager", "Production Manager"),
                            ("Video Editor", "Video Editor"),
                            ("Animator", "Animator"),
                            ("3D Designer/Artist", "3D Designer/Artist"),
                            ("Sound Designer", "Sound Designer"),
                            ("Photographer", "Photographer"),
                            ("Illustrator", "Illustrator"),
                        ],
                        default="Graphic Designer",
                        max_length=50,
                    ),
                ),
                ("photo", models.ImageField(blank=True, upload_to="static/photos/")),
                ("linkedin_url", models.URLField()),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="team.team"
                    ),
                ),
            ],
        ),
    ]
