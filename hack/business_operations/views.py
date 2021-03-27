from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework import status
from django.utils import timezone
import pandas
from itertools import chain
from django.utils.translation import gettext_lazy as _

from .models import *
from .serializers import CitySerializer, StoryImageSerializer, StorySerializer

from .models import City, StoryImage, Story


def input_bool(input_str):
    return input_str.lower() in ("yes", "true", "t", "1")


class GetCities(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class GetStories(generics.ListAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()
