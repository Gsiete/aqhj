from cities_light.abstract_models import (AbstractCity, AbstractRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals
import cities_light
from cities_light.settings import ICity, ICountry
from timezone_field import TimeZoneField
from django.dispatch import receiver
from django.db import models
import pytz
import logging

logger = logging.getLogger(__name__)


class Region(AbstractRegion):
    pass
connect_default_signals(Region)


class City(AbstractCity):
    timezone = TimeZoneField()

    @property
    def url(self):
        from main.functions import reverse_from_object
        try:
            return reverse_from_object('set-city', self)
        except:
            logger.error("Couldn't set city URL for %s with id: %s" % (self.slug, self.id))
            return ''

    def get_display_name(self):
        return '%s, %s' % (self.name, self.country.name)
connect_default_signals(City)


class Country(AbstractCountry):
    capital = models.ForeignKey(City, related_name='country_is_capital', null=True)
connect_default_signals(Country)


@receiver(cities_light.signals.city_items_post_import)
def set_city_fields(sender, instance, items, **kwargs):
    instance.timezone = pytz.timezone(items[ICity.timezone])


@receiver(cities_light.signals.country_items_post_import)
def process_country_import(sender, instance, items, **kwargs):
    try:
        capital = City.objects.get(name=items[ICountry.capital], country=instance.id)
    except:
        logger.error('Except: Capital:%s, country_id=%d' % (items[ICountry.capital], instance.id))
        return

    if capital is None:
        logger.error('None: Capital:%s, country_id=%d' % (items[ICountry.capital], instance.id))
        return

    instance.capital = City.objects.get(name=items[ICountry.capital], country__id=instance.id)
