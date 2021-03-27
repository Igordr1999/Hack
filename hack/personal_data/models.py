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


def set_random_name_for_image(image):
    if image:
        file_name, file_extension = os.path.splitext(image.name)
        if len(file_name) < 32:
            random_name = uuid.uuid4().hex + file_extension
            image.name = random_name
    return image


class Gender(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class ProfileManager(UserManager):
    pass


class Profile(AbstractUser):
    objects = ProfileManager()
    birthday = models.DateField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    patronymic = models.CharField(max_length=64, null=True, blank=True)

    def fullname(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.patronymic) \
            if self.patronymic else "{} {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.fullname()

    class Meta:
        ordering = ["last_name", "first_name", "patronymic"]
