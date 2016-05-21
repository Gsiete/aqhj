from datetime import timedelta

from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from redactor.fields import RedactorField

from cities.models import City


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=50, default='')
    logo = models.ImageField(upload_to='tournament/logo/', null=True, blank=True)

    @property
    def short(self):
        return self.short_name or self.name

    def __str__(self):
        return self.name


class Season(models.Model):
    tournament = models.ForeignKey(Tournament)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    start = models.DateTimeField('start of the tournament')
    end = models.DateTimeField('end of the tournament')

    @property
    def short(self):
        return '%s %s' % (self.tournament.short, self.name)

    def __str__(self):
        return '%s - %s' % (self.tournament.name, self.name)


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=150, blank=True, null=True)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#imagefield
class Team(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=50, default='')
    stadium = models.ForeignKey(Stadium)
    logo = models.ImageField(upload_to='team/logo/', null=True)
    is_domain_team = models.BooleanField('is the main team of the domain')

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"

    GAMES_IN_SEASON = ['Fase de grupo - Partido %d' % x for x in range(1, 4)] + \
                      ['Ronda de 16', 'Cuartos de final', 'Semi-final', 'Final'] + \
                      ['Fecha %d' % x for x in range(1, 40)]
    GAMES_IN_SEASON_CHOICES = [(slugify(gis), gis) for gis in GAMES_IN_SEASON]

    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_a')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_b')
    score_team_a = models.IntegerField(null=True, blank=True)
    detail_goals_team_a = models.CharField(null=True, blank=True, max_length=100)
    score_team_b = models.IntegerField(null=True, blank=True)
    detail_goals_team_b = models.CharField(null=True, blank=True, max_length=100)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    game_in_season = models.CharField(choices=GAMES_IN_SEASON_CHOICES, max_length=30, blank=True, null=True)
    time = models.DateTimeField('local time of the match')
    end_time = models.DateTimeField('time the match ends', null=True, blank=True)
    preview_part1 = RedactorField(blank=True)
    preview_part2 = RedactorField(blank=True)
    preview_part3 = RedactorField(blank=True)
    summary = RedactorField(blank=True)

    @property
    def team_a_winner(self):
        return self.score_team_a is not None and self.score_team_b is not None and self.score_team_a > self.score_team_b

    @property
    def team_b_winner(self):
        return self.score_team_a is not None and self.score_team_b is not None and self.score_team_a < self.score_team_b

    def stadium_time(self):
        return self.time.astimezone(self.stadium.city.timezone)

    @property
    def game_in_season_literal(self):
        return dict(self.GAMES_IN_SEASON_CHOICES)[self.game_in_season] if self.game_in_season else ''

    @property
    def match_status(self):
        if self.time < timezone.now():
            return 'before'
        elif self.time < timezone.now() < self.end_time:
            return 'ongoing'
        elif timezone.now() < self.time:
            return 'after'

    @property
    def is_today(self):
        return self.time - timedelta(1) > timezone.now() > self.end_time + timedelta(1)

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
