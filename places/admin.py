from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from tinymce.models import HTMLField

from places.models import Place, Image


# Register your models here.

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['place_image']
    extra = 3

    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />',
                           url=obj.image.url,
                           width=None,
                           height=200
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    fields = ['placeId', 'title', 'short_description', 'long_description', 'lng', 'lat']
    inlines = [ImageInline]
    content = HTMLField()


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['image', 'place']
    list_display_links = ['place']
