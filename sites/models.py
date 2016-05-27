from django.core.urlresolvers import get_urlconf, get_resolver
from django.db import models
from django.utils.decorators import classproperty


class RouteConfig(models.Model):
    @classproperty
    def routes(self):
        return [rt for rt in get_resolver(get_urlconf()).reverse_dict if isinstance(rt, str) and rt[0] != '_']

    is_published = models.BooleanField('indicates weather the Config is published or not', default=False)
    route = models.CharField(choices=routes, max_length=60)
    meta_description = models.TextField('Content for the meta with name="description"')
    title = models.TextField('Content for the head title tag')
    og_title = models.CharField('Content for the og:title tag', max_length=150)
    og_description = models.TextField('Content for the og:description tag')
    og_type = models.CharField('Content for the og:type tag', max_length=50)
    h1 = models.CharField('Content for the main page title', max_length=100)
    h3 = models.CharField('Content for the secondary page title', max_length=100)


    @property
    def short(self):
        return '%s %s' % (self.tournament.short, self.short_name or self.name)

    def __str__(self):
        return '%s - %s' % (self.route, self.name)

    class Meta:
        ordering = ["is_published"]
