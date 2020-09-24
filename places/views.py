import json
from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse, HttpResponse
from django.urls import reverse


def serialize_point(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse(place_by_id, args=[place.id])
        }
    }


def index(request):
    places = Place.objects.all()
    points = {
        "type": "FeatureCollection",
        "features": [serialize_point(place) for place in places]
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
    return JsonResponse(points, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
