# Generated by Django 4.1.6 on 2023-04-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0008_alter_article_tags_alter_tag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("Planning", "Planning"),
                    ("In progress", "In progress"),
                    ("Reviewing", "Reviewing"),
                    ("Completed", "Completed"),
                    ("Required", "Required"),
                ],
                default="Required",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                choices=[
                    ("Illustration", "Illustration"),
                    ("Web design", "Web design"),
                    ("Animation", "Animation"),
                    ("Branding", "Branding"),
                    ("Design trends", "Design trends"),
                    ("Graphic design", "Graphic design"),
                    ("User experience", "User experience"),
                    ("Design tools", "Design tools"),
                    ("Responsive design", "Responsive design"),
                    ("Design inspiration", "Design inspiration"),
                    ("UI/UX design", "UI/UX design"),
                    ("User interface", "User interface"),
                ],
                max_length=50,
            ),
        ),
    ]
