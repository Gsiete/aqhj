from django.conf.urls import url

from . import views

season_pattern = r'(?P<season__tournament__slug>[\w-]+)/(?P<season__slug>[\w-]+)'
match_pattern = season_pattern + r'/(?P<game_in_season>[\w-]+)/(?P<team_a__slug>[\w-]+)-vs-(?P<team_b__slug>[\w-]+)'
past_match_pattern = match_pattern + r'-(?P<score_team_a>[0-9]+)-(?P<score_team_b>[0-9]+)/resultado-goles-y-noticias'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^' + past_match_pattern + r'$', views.past_match, name='past_match'),
    url(r'^last-matches$', views.last_matches, name='last_matches'),
]
# https://docs.djangoproject.com/en/1.9/topics/http/urls/#including-other-urlconfs