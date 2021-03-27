from django.contrib import admin
from .models import City, Story, StoryImage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id']

