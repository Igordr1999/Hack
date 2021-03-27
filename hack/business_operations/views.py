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
from .serializers import CitySerializer, StoryImageSerializer, StorySerializer, GuideSerializer, RouteSerializer, \
    RouteCreateSerializer, ShortRouteSerializer

from .models import City, StoryImage, Story


def input_bool(input_str):
    return input_str.lower() in ("yes", "true", "t", "1")


class GetCities(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class GetStories(generics.ListAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class GuideView(generics.RetrieveAPIView):
    serializer_class = GuideSerializer

    def get_object(self):
        city_id = self.request.GET.get('city_id', '')
        city = get_object_or_404(City, id=city_id)
        guide = Guide.objects.filter(city=city).first()
        return guide


class RouteDetailView(generics.RetrieveAPIView):
    serializer_class = RouteSerializer

    def get_object(self):
        route_id = self.request.GET.get('route_id', '')
        route = get_object_or_404(Route, id=route_id)
        return route


class RouteListView(generics.ListAPIView):
    serializer_class = ShortRouteSerializer

    def get_queryset(self):
        print(self.request.user)
        routes = Route.objects.filter(profile=self.request.user)
        # routes = Route.objects.all()
        return routes


class RouteCreate(generics.CreateAPIView):
    serializer_class = RouteCreateSerializer
