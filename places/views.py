import json

from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import HttpResponse, Http404, JsonResponse
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


def place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    response_data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return HttpResponse(json.dumps(response_data, ensure_ascii=False, indent=4), content_type="application/json")