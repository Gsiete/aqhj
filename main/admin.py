from django.contrib import admin

from main.forms import StadiumForm
from .models import Match, Tournament, Team, Stadium, Season, TeamSeason, TeamSeasonGroup, Summary, ThreeArticles


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SiteRelAdmin(admin.ModelAdmin):
    list_filter = ('site',)


class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('stadium_time', 'url')
    list_filter = ('season',)
    list_display = ('team_a', 'team_b', 'time', 'season', 'game_in_season')


class TeamAdmin(SlugAdmin, SiteRelAdmin):
    list_display = ('__str__', 'stadium')


class StadiumAdmin(admin.ModelAdmin):
    form = StadiumForm
    list_display = ('__str__', 'city', 'short_name')


class SeasonAdmin(SlugAdmin):
    list_display = ('__str__', 'start', 'end', 'tournament')


class TeamSeasonAdmin(admin.ModelAdmin):
    list_display = ('team', 'season')


class TeamSeasonGroupAdmin(admin.ModelAdmin):
    list_display = ('team', 'season', 'group')


class ThreeArticlesAdmin(SiteRelAdmin):
    list_display = ('match', 'match_season_short', 'match_game_in_season', 'site', 'is_published')


class SummaryAdmin(SiteRelAdmin):
    list_display = ('match', 'match_season_short', 'match_game_in_season', 'site', 'is_published', 'title_shortened')


admin.site.register(Match, admin_class=MatchAdmin)
admin.site.register(Tournament, admin_class=SlugAdmin)
admin.site.register(Team, admin_class=TeamAdmin)
admin.site.register(Stadium, admin_class=StadiumAdmin)
admin.site.register(Season, admin_class=SeasonAdmin)
admin.site.register(TeamSeason, admin_class=TeamSeasonAdmin)
admin.site.register(TeamSeasonGroup, admin_class=TeamSeasonGroupAdmin)
admin.site.register(ThreeArticles, admin_class=ThreeArticlesAdmin)
admin.site.register(Summary, admin_class=SummaryAdmin)
