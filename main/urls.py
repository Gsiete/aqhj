from django.conf.urls import url

from django.views.generic.base import RedirectView, TemplateView

from . import views

season_part = r'(?P<season__tournament__slug>[\w-]+)/(?P<season__slug>[\w-]+)'
# gis = Game In Season
gis_part = r'/(?P<game_in_season>[a-z][\w-]+)'
no_gis_part = r'/(?P<time__month>[0-9]+)-(?P<time__day>[0-9-]+)'
match_part = r'/(?P<team_a__slug>[\w-]+)-vs-(?P<team_b__slug>[\w-]+)'
past_match_extra = r'-(?P<score_team_a>[0-9]+)-(?P<score_team_b>[0-9]+)/resultado-goles-y-noticias'

match_pattern = season_part + gis_part + match_part
match_pattern_no_gis = season_part + no_gis_part + match_part
past_match_pattern = match_pattern + past_match_extra
past_match_pattern_no_gis = match_pattern_no_gis + past_match_extra

season_pattern = season_part.replace('season__', '')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^' + match_pattern + r'/hoy$', views.match_before, name='match_today', kwargs={'today': True}),
    url(r'^' + match_pattern + r'$', views.match_before, name='match_before'),
    url(r'^' + match_pattern_no_gis + r'/hoy$', views.match_before, name='match_today_no_gis', kwargs={'today': True}),
    url(r'^' + match_pattern_no_gis + r'$', views.match_before, name='match_before_no_gis'),
    url(r'^' + past_match_pattern + r'$', views.past_match, name='past_match'),
    url(r'^' + past_match_pattern_no_gis + r'$', views.past_match, name='past_match_no_gis'),
    url(r'^resultados/como-salio-argentina$', views.last_matches, name='last_matches'),
    url(r'^' + season_pattern + r'/fase-de-grupos/posiciones$', views.group_round_positions, name='group_positions'),
    url(r'^completar-subscripcion$',  TemplateView.as_view(template_name='main/thanks.html'), name='nl_success_confirm'),
    url(r'^sitemap\.xml$',  TemplateView.as_view(template_name='main/sitemap.xml', content_type='text/xml'), name='sitemap'),
    url(r'^robots\.txt$',  TemplateView.as_view(template_name='main/robots.txt', content_type='text/plain'), name='robots'),
    url(r'^BingSiteAuth\.xml$',  TemplateView.as_view(template_name='BingSiteAuth.xml', content_type='text/xml'), name='BingSiteAuth'),
]
# https://docs.djangoproject.com/en/1.9/topics/http/urls/#including-other-urlconfs
