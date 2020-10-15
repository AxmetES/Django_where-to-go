import logging
import requests
from django.core.management.base import BaseCommand
from urllib.parse import urlparse
from django.core.files.base import ContentFile

from places.models import Place, Image


def get_filename(url):
    url_fragments = urlparse(url)
    file_name = url_fragments.path.split('/')[-1]
    return file_name


def replace_bd_id(images):
    names = []
    obj_to_str = [image.image.__str__() for image in images]
    for image in obj_to_str:
        name_id, extend = image.split('.')
        name, bd_id = name_id.split('_')
        file_name = name + '.' + extend
        names.append(file_name)
    return names


class Command(BaseCommand):
    help = 'Load json file by the url in database.'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        response_data = response.json()
        title = response_data['title']
        short_description = response_data['description_short']
        long_description = response_data['description_long']
        lng = response_data['coordinates']['lng']
        lat = response_data['coordinates']['lat']

        place, is_created = Place.objects.update_or_create(title=title, short_description=short_description, lng=lng,
                                                           lat=lat, defaults={'long_description': long_description})
        images_url = response_data['imgs']
        if not is_created:
            place_images = place.images.all()
            place_images.delete()

        for num, url in enumerate(images_url):
            image = Image.objects.create(place=place, position=num)
            response_img = requests.get(url)
            response_img.raise_for_status()
            content = ContentFile(response_img.content)
            file_name = get_filename(url)
            image.image.save(file_name, content, True)


if __name__ == '__main__':
    logging.basicConfig(filename="logfile.log", level=logging.INFO)
