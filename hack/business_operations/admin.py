from django.contrib import admin
from .models import City, Story, StoryImage, GuideBlock, Guide


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(GuideBlock)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'preview_image', 'created', 'created', 'author', 'rating']
