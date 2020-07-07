from django.contrib import admin
from places.models import Place, Image


# Register your models here.

@admin.register(Place)
class PlaseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    fields = ('placeId', 'title', 'description_short', 'description_long', 'lng', 'lat')
    readonly_fields = ('id',)


class Place_title(admin.TabularInline):
    model = Place
    fk_name = 'title'


@admin.register(Image)
class imageAdmin(admin.ModelAdmin):
    inline = [Place_title, ]
    fields = ('image', 'place')
