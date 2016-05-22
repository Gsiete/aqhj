from django.contrib import admin
from .models import Match, Tournament, Team, Stadium, Season, TeamSeason


class MainAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('stadium_time', 'url')

admin.site.register(Match, admin_class=MatchAdmin)
admin.site.register(Tournament, admin_class=MainAdmin)
admin.site.register(Team, admin_class=MainAdmin)
admin.site.register(Stadium)
admin.site.register(Season, admin_class=MainAdmin)
admin.site.register(TeamSeason)
