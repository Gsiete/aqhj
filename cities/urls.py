from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajax/city-autocomplete/$', views.CityAutocomplete.as_view(), name='city-autocomplete'),
]