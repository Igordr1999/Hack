from rest_framework import serializers
from .models import City, StoryImage, Story, GuideBlock, Guide
from personal_data.serializers import ProfileFullnameSerializer


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


class GuideBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideBlock
        fields = ('id', 'title', 'description', 'image')


class GuideSerializer(serializers.ModelSerializer):
    blocks = GuideBlockSerializer(many=True)
    author = ProfileFullnameSerializer()

    class Meta:
        model = Guide
        fields = ('id', 'title', 'description', 'preview_image',
                  'created', 'author', 'rating', 'blocks')

