from cities_light.abstract_models import (AbstractCity, AbstractRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals
import cities_light
from cities_light.settings import ICity, ICountry
from timezone_field import TimeZoneField
from django.dispatch import receiver
from django.db import models
import pytz


class Region(AbstractRegion):
    pass
connect_default_signals(Region)


class City(AbstractCity):
    timezone = TimeZoneField()

    def get_display_name(self):
        return '%s, %s' % (self.name, self.country.name)
connect_default_signals(City)


class Country(AbstractCountry):
    capital = models.ForeignKey(City, related_name='country_is_capital')
connect_default_signals(Country)

@receiver(cities_light.signals.city_items_post_import)
def set_city_fields(sender, instance, items, **kwargs):
    instance.timezone = pytz.timezone(items[ICity.timezone])


@receiver(cities_light.signals.country_items_post_import)
def process_country_import(sender, instance, items, **kwargs):
    instance.capital = City.objects.get(name=items[ICountry.capital], country=instance)