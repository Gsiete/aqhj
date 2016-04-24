from django.conf import settings
from django.db import models
from timezone_field import TimeZoneField


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    start_date = models.DateTimeField('start of the tournament')
    end_date = models.DateTimeField('end of the tournament')

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    timezone = TimeZoneField(default='Europe/Madrid')

    def __str__(self):
        return self.name


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#imagefield
class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')
    stadium = models.ForeignKey(Stadium)
    is_domain_team = models.BooleanField('is the main team of the domain')

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"

    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_a')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='matches_as_b')
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField('local time of the match')

    def stadium_time(self):
        return self.time.astimezone(self.stadium.timezone)

    def __str__(self):
        return str(self.team_a) + ' - ' + str(self.team_b) + ' (' + str(self.time) + ')'
