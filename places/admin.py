from django.contrib import admin
from places.models import Place


# Register your models here.

@admin.register(Place)
class PlaseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    fields = ('title', 'description_short', 'description_long', 'lng', 'lat',)
