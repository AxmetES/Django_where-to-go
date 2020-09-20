from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    placeId = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    short_description = models.CharField(max_length=200, blank=True, verbose_name="Короткое описание")
    long_description = tinymce_models.HTMLField(blank=True, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")


class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField(null=True, blank=True, verbose_name='Позиция')

    class Meta(object):
        ordering = ['position']
