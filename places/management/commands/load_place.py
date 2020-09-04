import pprint
from io import BytesIO
from django.core.management.base import BaseCommand
import requests
from urllib.parse import urlparse
from PIL import Image
from django.core.files.base import ContentFile

from places.models import Place, Image


def get_filename(url):
    parsed = urlparse(url)
    file = parsed.path.split('/')[-1]
    return file


class Command(BaseCommand):
    help = 'Load json file by the url in database.'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        response_data = response.json()
        title = response_data['title']
        short_description = response_data['description_short']
        long_description = response_data['description_long']
        lng = response_data['coordinates']['lng']
        lat = response_data['coordinates']['lat']

        Place.objects.get_or_create(title=title, short_description=short_description,
                                    long_description=long_description,
                                    lng=lng, lat=lat)
        place = Place.objects.filter(title=title)

        imge = response_data['imgs']

        for num, url in enumerate(imge):
            image = Image.objects.create(place=place[0], position=num)
            response_imge = requests.get(url)
            content = ContentFile(response_imge.content)
            file_name = get_filename(url)
            image.image.save(file_name, content, True)
