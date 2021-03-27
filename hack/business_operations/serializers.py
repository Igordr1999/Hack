from rest_framework import serializers
from .models import City, StoryImage, Story


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class StoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryImage
        fields = ('id', 'image')


class StorySerializer(serializers.ModelSerializer):
    images = StoryImageSerializer(many=True)

    class Meta:
        model = Story
        fields = ('id', 'circle_title', 'circle_image', 'images')
