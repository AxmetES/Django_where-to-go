from django.shortcuts import render
from places.models import Place
import pprint


def serialaized_place(places):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [places.lng, places.lat]
        },
        "properties": {
            "title": places.title,
            "placeId": places.placeId,
            "detailsUrl": "{% static 'places/place.json' %}"
        }
    }


def index(request):
    places = Place.objects.all()
    points = {
        "type": "FeatureCollection",
        "features": [serialaized_place(place) for place in places]
    }
    pprint.pprint(points)
    context = {
        "points": points
    }
    return render(request, 'index.html', context)
