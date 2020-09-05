from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    placeId = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = tinymce_models.HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(default='default')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField(null=True, blank=True)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.place}'
