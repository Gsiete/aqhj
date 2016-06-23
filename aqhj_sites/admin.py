from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import DomainConfig, RouteConfig, RedirectOn404


class SitesModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '75'})},
    }


admin.site.register(RouteConfig, SitesModelAdmin)
admin.site.register(DomainConfig, SitesModelAdmin)
admin.site.register(RedirectOn404, SitesModelAdmin)
