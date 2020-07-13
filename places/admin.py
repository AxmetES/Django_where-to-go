from django.contrib import admin
from django.utils.html import format_html_join, format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image


# Register your models here.


def get_proportion(width, height):
    max_height = 200
    if width > height:
        ratio = max_height / width
    else:
        ratio = max_height / height
    new_width = ratio * width
    new_height = ratio * height
    return new_width, new_height


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ('place_image',)

    def place_image(self, obj):
        width = obj.image.width
        height = obj.image.height
        new_width, new_height = get_proportion(width, height)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=new_width,
            height=new_height
        )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    fields = ('placeId', 'title', 'description_short', 'description_long', 'lng', 'lat')
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_image', ]

    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=120,
        )
        )
