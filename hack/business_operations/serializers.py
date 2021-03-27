from rest_framework import serializers
from .models import City, StoryImage, Story, GuideBlock, Guide, GuideBlockImage, Route
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


class GuideBlockImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideBlockImage
        fields = ('id', 'image')


class GuideBlockSerializer(serializers.ModelSerializer):
    carousel = GuideBlockImageSerializer(many=True)

    class Meta:
        model = GuideBlock
        fields = ('id', 'title', 'description', 'image', 'carousel')


class GuideSerializer(serializers.ModelSerializer):
    blocks = GuideBlockSerializer(many=True)
    author = ProfileFullnameSerializer()

    class Meta:
        model = Guide
        fields = ('id', 'title', 'description', 'preview_image',
                  'created', 'author', 'rating',
                  'is_news', 'is_event', 'lat', 'lon', 'event_date', 'blocks')


class ShortGuideSerializer(serializers.ModelSerializer):
    author = ProfileFullnameSerializer()

    class Meta:
        model = Guide
        fields = ('id', 'title', 'description', 'preview_image',
                  'created', 'author', 'rating',
                  'is_news', 'is_event', 'lat', 'lon', 'event_date')


class RouteSerializer(serializers.ModelSerializer):
    profile = ProfileFullnameSerializer()
    steps = GuideSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'profile', 'steps', 'paid')


class ShortRouteSerializer(serializers.ModelSerializer):
    profile = ProfileFullnameSerializer()
    steps = ShortGuideSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'profile', 'steps', 'paid')


class RouteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('id', 'profile', 'steps', 'paid')
