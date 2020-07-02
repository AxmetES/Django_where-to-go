from django.db import models


class Place(models.Model):
    placeId = models.TextField(default='default')
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()


class Image(models.Model):
    image = models.ImageField()
