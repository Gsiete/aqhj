from django.conf import settings
from django.db import models
from cities.models import City


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    logo = models.ImageField(upload_to='tournament/logo/', null=True, blank=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    tournament = models.ForeignKey(Tournament)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    start = models.DateTimeField('start of the tournament')
    end = models.DateTimeField('end of the tournament')

    def __str__(self):
        return '%s - %s' % self.tournament.name, self.name


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#imagefield
class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    stadium = models.ForeignKey(Stadium)
    logo = models.ImageField(upload_to='team/logo/', null=True)
    is_domain_team = models.BooleanField('is the main team of the domain')

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"
    GAMES_IN_SEASON = ['Fecha %d' % x for x in range(1, 40)] + ['Ronda de 16' + 'Cuartos de final' + 'Semi-final' + 'Final']

    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_a')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_b')
    score_team_a = models.IntegerField(null=True, blank=True)
    score_team_b = models.IntegerField(null=True, blank=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    game_in_season = models.CharField(choices=GAMES_IN_SEASON)
    time = models.DateTimeField('local time of the match')

    def stadium_time(self):
        return self.time.astimezone(self.stadium.city.timezone)

    def __str__(self):
        return str(self.team_a) + ' - ' + str(self.team_b) + ' (' + str(self.time) + ')'


class TeamSeason(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    matches_played = models.IntegerField(null=True, blank=True)
    wins = models.IntegerField(null=True, blank=True)
    draws = models.IntegerField(null=True, blank=True)
    losses = models.IntegerField(null=True, blank=True)
    goals_for = models.IntegerField(null=True, blank=True)
    goals_against = models.IntegerField(null=True, blank=True)
    goals_difference = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
