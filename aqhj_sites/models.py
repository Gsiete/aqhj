from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models


def find_routes():
    from main.urls import urlpatterns
    return [route.name for route in urlpatterns if route.name[0] != '_']


class SiteConfig(models.Model):
    is_published = models.BooleanField('indicates weather the Config is published or not', default=False)
    domain = models.CharField(choices=zip(*[settings.ALLOWED_HOSTS]*2), max_length=60)

    def og_fields(self):
        return dict((f.replace('og_', 'og:'), getattr(self, f)) for f in self._meta.get_fields() if f[:3] == 'og_')

    class Meta:
        abstract = True
        ordering = ["is_published"]


class RouteConfig(SiteConfig):
    route = models.CharField(choices=zip(*[find_routes()]*2), max_length=60)
    meta_description = models.TextField('Content for the meta with name="description"', blank=True, null=True)
    title = models.CharField('Content for the head meta title tag(<title>)', blank=True, null=True, max_length=250)
    og_title = models.CharField('Content for the og:title tag', blank=True, null=True, max_length=250)
    og_description = models.TextField('Content for the og:description tag', blank=True, null=True)
    og_type = models.CharField('Content for the og:type tag', blank=True, null=True, max_length=50)
    h1 = models.CharField('Content for the main page title (h1)', blank=True, null=True, max_length=200)
    h3 = models.CharField('Content for the secondary page title (h3)', blank=True, null=True, max_length=200)

    def __str__(self):
        return '%s - %s Published: %s' % (self.domain, self.route, self.is_published)

    class Meta:
        ordering = ["is_published"]


class DomainConfig(SiteConfig):
    og_locale = models.CharField('Content for the og:locale tag', max_length=8, blank=True, null=True)
    og_site_name = models.CharField('Content for the og:site_name tag', blank=True, null=True, max_length=50)
    facebook_url = models.CharField('facebook url (page, group or whatever)', blank=True, null=True, max_length=150)
    twitter_url = models.CharField('url for the twitter Channel', blank=True, null=True, max_length=100)
    bing_validation_meta = models.CharField('validation code to put into te bing validation meta', blank=True,
                                            null=True, max_length=100)
    google_analytics_script = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s Published: %s' % (self.domain, self.is_published)

    class Meta:
        ordering = ["is_published"]
