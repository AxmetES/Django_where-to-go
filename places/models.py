from django.db import models


class Place(models.Model):
    placeId = models.TextField(null=True)
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', null=True, default=None)

    def __str__(self):
        return f'{self.place}'
