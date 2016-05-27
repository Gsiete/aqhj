from django.contrib import admin

from .models import DomainConfig, RouteConfig


admin.site.register(RouteConfig)
admin.site.register(DomainConfig)
