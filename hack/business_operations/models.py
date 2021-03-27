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
