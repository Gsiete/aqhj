from django.contrib import admin
from .models import Match, Tournament, Team, Stadium, Season, TeamSeason, TeamSeasonGroup, Summary, ThreeArticles


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SiteRelAdmin(admin.ModelAdmin):
    list_filter = ('site',)


class SlugSiteRelAdmin(SlugAdmin, SiteRelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('stadium_time', 'url')
    list_filter = ('season',)

admin.site.register(Match, admin_class=MatchAdmin)
admin.site.register(Tournament, admin_class=SlugAdmin)
admin.site.register(Team, admin_class=SlugSiteRelAdmin)
admin.site.register(Stadium)
admin.site.register(Season, admin_class=SlugAdmin)
admin.site.register(TeamSeason)
admin.site.register(TeamSeasonGroup)
admin.site.register(ThreeArticles, admin_class=SiteRelAdmin)
admin.site.register(Summary, admin_class=SiteRelAdmin)
