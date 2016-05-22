from django.conf.urls import url

from . import views

season_pattern = r'(?P<season__tournament__slug>[\w-]+)/(?P<season__slug>[\w-]+)'
match_pattern = season_pattern + r'/(?P<game_in_season>[\w-]+)/(?P<team_a__slug>[\w-]+)-vs-(?P<team_b__slug>[\w-]+)'
past_match_pattern = match_pattern + r'-(?P<score_team_a>[0-9]+)-(?P<score_team_b>[0-9]+)/resultado-goles-y-noticias'
season_pattern_for_season = r'(?P<tournament__slug>[\w-]+)/(?P<slug>[\w-]+)'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^' + past_match_pattern + r'$', views.past_match, name='past_match'),
    url(r'^' + match_pattern + r'/hoy$', views.match_before, name='match_today', kwargs={'hoy': True}),
    url(r'^' + match_pattern + r'$', views.match_before, name='match_before'),
    url(r'^ultimos-resultados$', views.last_matches, name='last_matches'),
    url(r'^' + season_pattern_for_season + r'/ronda-de-grupos/posiciones$', views.group_round_positions, name='group_positions'),
]
# https://docs.djangoproject.com/en/1.9/topics/http/urls/#including-other-urlconfs