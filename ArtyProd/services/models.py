from django.db import models


class Service(models.Model):
    typeService = [
        ("Logo Design", "Logo Design"),
        ("Web Design", "Web Design"),
        ("Video Production", "Video Production"),
        ("Animation", "Animation"),
        ("3D Modeling", "3D Modeling"),
    ]
    name = models.CharField(choices=typeService, default="Web Design", max_length=50)
    description = models.TextField(default="Empty")

    def __str__(self):
        return self.name
