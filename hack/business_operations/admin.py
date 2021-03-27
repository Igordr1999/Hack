from django.contrib import admin
from .models import City, Story, StoryImage, GuideBlock, Guide, GuideBlockImage, Route, GuideCategory


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(GuideCategory)
class GuideCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']


@admin.register(GuideBlockImage)
class GuideBlockImageAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(GuideBlock)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'preview_image', 'created', 'created', 'author', 'rating']


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'paid']
