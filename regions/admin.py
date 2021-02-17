from django.contrib import admin
from .models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=("id","code","name",'arabic_name')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display=("id","code","name","arabic_name")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("id","postal_code","name","arabic_name","region")
