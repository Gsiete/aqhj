from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajax-autocompletar$', views.CityAutocomplete.as_view(), name='city-autocomplete'),
    url(r'^(?P<slug>[\w-]+)/(?P<country__slug>[\w-]+)$', views.set_city, name='set-city'),
]