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
        if obj.image:
            return format_html('<img src="{url}" height={height} />',
                               url=obj.image.url,
                               height=200
                               )
        else:
            return 'Здесь будет превью, когда вы выберете файл.'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    fields = ['title', 'short_description', 'long_description', 'lng', 'lat']
    inlines = [ImageInline]
    content = HTMLField()


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['image', 'place']
    list_display_links = ['place']
