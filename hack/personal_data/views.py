from .models import Gender, Profile
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.db.models import Q

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from django.utils import timezone
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
import requests


def my_auth(profile):
    if profile.is_active:
        activate("ru")
        profile.last_login = timezone.now()
        profile.save()
        refresh = RefreshToken.for_user(profile)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return JsonResponse({"detail": _("User is not active")}, status=status.HTTP_403_FORBIDDEN)


class GetFullname(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileFullnameSerializer

    def get_object(self):
        return self.request.user


class Auth(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        profile = get_object_or_404(Profile, username=username)
        true_password = profile.check_password(raw_password=password)
        if not true_password:
            return JsonResponse({"detail": _("Invalid password")}, status=status.HTTP_404_NOT_FOUND)
        return my_auth(profile=profile)
