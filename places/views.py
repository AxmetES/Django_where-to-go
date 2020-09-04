import json
from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import HttpResponse
from django.urls import reverse


def serialaized_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.placeId,
            "detailsUrl": reverse(place_by_id, args=[place.id])
        }
    }


def index(request):
    places = Place.objects.all()
    points = {
        "type": "FeatureCollection",
        "features": [serialaized_place(place) for place in places]
    }
    context = {
        "points": points
    }
    return render(request, 'index.html', context)


def place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    points = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return HttpResponse(json.dumps(points, ensure_ascii=False, indent=4), content_type="application/json")
