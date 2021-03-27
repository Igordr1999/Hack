from rest_framework import serializers
from .models import Gender, Profile


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'name', 'code')


class ProfileFullnameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'last_name', 'first_name', 'patronymic')
