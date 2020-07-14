from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    placeId = models.TextField(null=True)
    title = models.TextField()
    description_short = models.TextField()
    description_long = tinymce_models.HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', default=True)
    position = models.PositiveIntegerField(null=True, blank=True)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.place}'
