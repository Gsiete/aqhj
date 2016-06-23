from datetime import timedelta
from html import escape

from django.contrib.sites.models import Site
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
    short_name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, default='')
    start = models.DateTimeField('start of the tournament')
    end = models.DateTimeField('end of the tournament')
    is_main = models.BooleanField('indicate that this season is currently the main in the domain')
    groups_og_image = models.ImageField(upload_to='season/groups_og/', null=True, blank=True)
    results_image = models.ImageField('Results OG image', upload_to='season/results/', null=True, blank=True)

    @property
    def short(self):
        return '%s %s' % (self.tournament.short, self.short_name or self.name)

    def __str__(self):
        return '%s %s' % (self.tournament.name, self.name)


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=150, blank=True, null=True)
    city = models.ForeignKey(City)

    @property
    def short(self):
        return self.short_name or self.name

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
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"
        ordering = ["-time"]

    GAMES_IN_SEASON = ['Fase de grupo - Partido %d' % x for x in range(1, 4)] + \
                      ['Ronda de 16', 'Cuartos de final', 'Semi-final', 'Final'] + \
                      ['Fecha %d' % x for x in range(1, 40)]
    GAMES_IN_SEASON_CHOICES = [(slugify(gis), gis) for gis in GAMES_IN_SEASON]

    is_published = models.BooleanField(default=False)
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
    end_time = models.DateTimeField('time the match ends')
    og_image = models.ImageField(upload_to='season/og/', null=True, blank=True)
    html_video = models.TextField(null=True, blank=True,
                                  help_text=escape('<iframe width="360" height="203" src="https://www.youtube.com/embed/CODIGO_DEL_VIDEO" frameborder="0" allowfullscreen=""></iframe>'))

    @property
    def team_a_winner(self):
        return self.score_team_a is not None and self.score_team_b is not None and self.score_team_a > self.score_team_b

    @property
    def team_b_winner(self):
        return self.score_team_a is not None and self.score_team_b is not None and self.score_team_a < self.score_team_b

    @property
    def stadium_time(self):
        return self.time.astimezone(self.stadium.city.timezone)

    @property
    def game_in_season_literal(self):
        return dict(self.GAMES_IN_SEASON_CHOICES)[self.game_in_season] if self.game_in_season else ''

    @property
    def match_status(self):
        if self.time is None:
            return None
        if timezone.now() < self.time:
            return 'before'
        if self.end_time and self.time < timezone.now() < self.end_time:
            return 'ongoing'
        if self.time < timezone.now():
            return 'after'

    @property
    def is_today(self):
        return self.time - timedelta(1) < timezone.now() < self.end_time + timedelta(1)

    @property
    def url(self):
        from main.functions import reverse_from_object
        if self.time is None:
            return None

        route = None
        if self.match_status == 'before':
                route = 'match_before'
        elif self.match_status == 'ongoing':
                route = 'match_before'
        elif not self.ready_for_review:
                route = 'match_before'
        elif self.match_status == 'after':
                route = 'past_match'

        if self.game_in_season is None and route:
            route += '_no_gis'

        return reverse_from_object(route, self) if route else None

    def ready_for_review(self):
        return self.score_team_a is not None and self.score_team_b is not None

    def team_local(self):
        return self.team_b if self.team_b.stadium == self.stadium else self.team_a

    def team_visitor(self):
        return self.team_a if self.team_b.stadium == self.stadium else self.team_b

    def team_domain(self):
        return self.team_b if self.team_b.is_domain_team else self.team_a

    def team_not_domain(self):
        return self.team_a if self.team_b.is_domain_team else self.team_b

    def score_local(self):
        return self.score_team_b if self.team_b.stadium == self.stadium else self.score_team_a

    def score_visitor(self):
        return self.score_team_a if self.team_b.stadium == self.stadium else self.score_team_b

    def score_domain(self):
        return self.score_team_b if self.team_b.is_domain_team else self.score_team_a

    def score_not_domain(self):
        return self.score_team_a if self.team_b.is_domain_team else self.score_team_b

    @property
    def hoy(self):
        return ' hoy' if self.is_today else ''

    def __str__(self):
        return str(self.team_a) + ' - ' + str(self.team_b) + ' (' + str(self.time) + ')'


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    priority_in_home = models.IntegerField(blank=True, null=True)
    image_home = models.ImageField(upload_to='article/image/', null=True, blank=True)
    title_short = models.CharField('Short Title (to be shown in home)', blank=True, null=True, max_length=250)
    content_short = RedactorField('Short Content (to be shown in home)', blank=True, null=True)

    def __str__(self):
        return str(self.site) + ' - ' + str(self.match)

    def title_home(self):
        return self.title_short

    def content_home(self):
        return self.content_short

    def match_game_in_season(self):
        return self.match.game_in_season_literal if self.match else ''

    def match_season_short(self):
        return self.match.season.short if self.match else ''

    class Meta:
        ordering = ["-created_at"]


class LinkArticle(Article):
    link = models.CharField(blank=True, null=True, max_length=250)


class ThreeArticles(Article):
    preview_part1 = RedactorField(blank=True)
    preview_part2 = RedactorField(blank=True)
    preview_part3 = RedactorField(blank=True)


class Summary(Article):
    title = models.CharField(blank=True, null=True, max_length=250)
    sub_title = models.CharField(blank=True, null=True, max_length=350)
    content = RedactorField(blank=True)

    def title_shortened(self):
        if len(self.title) > 50:
            return self.title[:49] + '…'
        else:
            return self.title[:50]

    def title_home(self):
        return self.title_short or self.title


class TeamSeasonAbstract(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    wins = models.IntegerField(null=True, blank=True)
    draws = models.IntegerField(null=True, blank=True)
    losses = models.IntegerField(null=True, blank=True)
    goals_for = models.IntegerField(null=True, blank=True)
    goals_against = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team) + ' - ' + str(self.season.short)

    @property
    def matches_played(self):
        return self.wins + self.draws + self.losses

    @property
    def goals_difference(self):
        return self.goals_for - self.goals_against

    @property
    def points(self):
        return self.wins*3 + self.draws

    class Meta:
        abstract = True
        ordering = ["position"]


class TeamSeason(TeamSeasonAbstract):
    pass


class TeamSeasonGroup(TeamSeasonAbstract):
    group = models.CharField(max_length=1)

    class Meta:
        ordering = ["group", "position"]