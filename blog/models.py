from django.conf import settings
from django.db import models
from django.utils import timezone

class Movies(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField("Actors")
    description = models.TextField(max_length=400,default="")
    directors = models.ManyToManyField("Directors")

    def __str__(self):
        return self.name

class Actors(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    text = models.TextField()
    date_of_birth = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title

class Directors(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    text = models.TextField()
    date_of_birth = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title