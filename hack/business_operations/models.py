import os

from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import Group

from django.conf import settings
import string
from random import randrange
from datetime import timedelta
from datetime import datetime
from django.utils import translation
import random
from django.core.files.temp import NamedTemporaryFile
import shutil
import requests
import uuid
from django.utils.translation import gettext_lazy as _
from personal_data.models import Profile


class City(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class StoryImage(models.Model):
    image = models.ImageField(upload_to="storyimage/", null=True, blank=True)


class Story(models.Model):
    circle_title = models.CharField(max_length=32)
    circle_image = models.ImageField(upload_to="story/", null=True, blank=True)
    images = models.ManyToManyField(StoryImage)

    def __str__(self):
        return self.circle_title

    class Meta:
        ordering = ["circle_title"]


class GuideBlockImage(models.Model):
    image = models.ImageField(upload_to="guideblockimage/", null=True, blank=True)


class GuideBlock(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="guideblock/", null=True, blank=True)
    carousel = models.ManyToManyField(GuideBlockImage)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Guide(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=500)
    preview_image = models.ImageField(upload_to="guidepreviewimage/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(default=5)
    blocks = models.ManyToManyField(GuideBlock)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
