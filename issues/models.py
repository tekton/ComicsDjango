from django.db import models
from django.contrib.auth.models import User

class Series(models.Model):
    '''
        To really keep track of things, every book needs to be part of a series;
        the hard part is going to be graphic novels but those should be their own model type with a list of series/issues
    '''
    name = models.CharField(max_length=255)
    volume = models.CharField(max_length=255, blank=True, null=True)
    mini_series_flag = models.BooleanField(default=False)
    series_max = models.CharField(max_length=255, blank=True, null=True)  # useful for old series and mini series, a la Flashpoint
    publisher = models.CharField(max_length=255, blank=True, null=True)  # could turn in to a select given how few there really are
    new52_flag = models.BooleanField(default=False)
    marvel_now = models.BooleanField(default=False)
    front_page = models.BooleanField(default=False)
    alt_search_text = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('issues.views.browse', [str(self.id)])

    def __unicode__(self):
        if self.volume:
            v_str = " v" + str(self.volume)
        else:
            v_str = ""

        rtn_str = str(self.name) + v_str
        if self.new52_flag is True:
            rtn_str += " (New 52)"
        if self.marvel_now is True:
            rtn_str += "(Marvel NOW!)"
        return rtn_str


class Comic(models.Model):
    '''
        this class is for the actual issues/series management side of things
    '''
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.FloatField()  # ususally numbers, but there's a decent amount of A, B, C, etc
    year = models.CharField(max_length=255, blank=True, null=True)  # should be a date or year stamp
    series = models.ForeignKey(Series)
    read = models.BooleanField(default=False)
    own = models.BooleanField(default=False)
    annual = models.BooleanField(default=False)
    annual_number = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        rtn_str = str(self.series.name) + " " + str(self.number)
        if self.series.new52_flag is True:
            rtn_str += " (New 52)"
        if self.series.marvel_now is True:
            rtn_str += "(Marvel NOW!)"
        return rtn_str


class Ratings(models.Model):
    user = models.ForeignKey(User)
    comic = models.ForeignKey(Comic, null=True, blank=True)
    art = models.FloatField(blank=True, null=True)
    story = models.FloatField(blank=True, null=True)
    overall = models.FloatField(blank=True, null=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'comic')
