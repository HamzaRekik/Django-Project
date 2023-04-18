
from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Personne(models.Model):
    POSTS = [
        ('Graphic Designer','Graphic Designer'),
        ('Web Designer' ,'Web Designer'),
        ('UI/UX Designer','UI/UX Designer'),
        ('Creative Director','Creative Director'),
        ('Art Director','Art Director'),
        ('Copywriter','Copywriter'),
        ('Social Media Manager','Social Media Manager'),
        ('Marketing Manager','Marketing Manager'),
        ('Project Manager','Project Manager'),
        ('Account Manager','Account Manager'),
        ('Production Manager','Production Manager'),
        ('Video Editor','Video Editor'),
        ('Animator','Animator'),
        ('3D Designer/Artist','3D Designer/Artist'),
        ('Sound Designer','Sound Designer'),
        ('Photographer','Photographer'),
        ('Illustrator','Illustrator')
    ]
    name = models.CharField( max_length=50)
    file_cv = models.FileField( upload_to='static/cv/', max_length=100 , blank=True)
    post = models.CharField(choices=POSTS, max_length=50 , default='Graphic Designer')
    photo = models.ImageField( upload_to='static/photos/' , blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE )
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name
    
