# Generated by Django 4.1.5 on 2023-04-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('Animation', 'Animation'), ('Illustration', 'Illustration'), ('Branding', 'Branding'), ('Design trends', 'Design trends'), ('Design tools', 'Design tools'), ('Graphic design', 'Graphic design'), ('User interface', 'User interface'), ('Web design', 'Web design'), ('Responsive design', 'Responsive design'), ('Design inspiration', 'Design inspiration'), ('User experience', 'User experience'), ('UI/UX design', 'UI/UX design')], max_length=50),
        ),
    ]