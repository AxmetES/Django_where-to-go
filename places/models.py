from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    short_description = models.TextField(blank=True, verbose_name="Короткое описание")
    long_description = tinymce_models.HTMLField(blank=True, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images", verbose_name="Место")
    position = models.PositiveIntegerField(blank=True, verbose_name="Позиция")

    def __str__(self):
        return str(self.image)

    class Meta(object):
        ordering = ['position']
