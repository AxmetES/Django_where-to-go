from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    placeId = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=200)
    description_long = tinymce_models.HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', default=True)
    position = models.PositiveIntegerField(null=True, blank=True)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.place}'
