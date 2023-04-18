from django.db import models
from services.models import *
from team.models import *
# Create your models here.

class Project(models.Model):
    DONE = [('Planning','Planning'),('In progress','In progress'),('Reviewing','Reviewing'),('Completed','Completed'),('Suggested','Suggested')]
    libelle = models.CharField( max_length=50)
    type = models.ManyToManyField(Service ,blank=True)
    description = models.TextField()
    details = models.FileField(upload_to='static/details/')
    image = models.ImageField(upload_to='static/photos/')
    team = models.OneToOneField(Team, on_delete=models.CASCADE ,null=True)
    dateD = models.DateField(auto_now_add=True)
    dateF = models.DateField(blank=True, null=True)
    status = models.CharField(choices=DONE, max_length=50 , default='Suggested')

    def __str__(self):
        return self.libelle
