from django.contrib import admin
from .models import Gender, Profile


@admin.register(Gender)
class GenderTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(Profile)
class GenderTaskAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
