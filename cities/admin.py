from cities_light.admin import CityAdmin
from django.contrib import admin

CityAdmin.readonly_fields = ('url',)
