from django.db import models


class Place(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
