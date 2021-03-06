from django.db import models
from django.contrib.auth.models import User
from issues.models import Comic, Series


class RootFolder(models.Model):
    uri = models.CharField(max_length=255)
    last_scanned = models.DateTimeField(blank=True, null=True)
    primary = models.BooleanField(default=False)
    os_blob = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.uri


class TransferRoot(models.Model):
    uri = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="none")

    def __unicode__(self):
        return self.uri


class ComicFile(models.Model):
    # The one things they'll all have...when you combine them!
    name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    # Should have,  but in case they're not needed for some reason...
    rootFolder = models.ForeignKey(RootFolder, blank=True, null=True)
    folderPath = models.CharField(max_length=255, blank=True, null=True)
    extension = models.CharField(max_length=255, blank=True, null=True)
    # Parsing potential...
    error_flag = models.BooleanField(default=False)
    review_flag = models.BooleanField(default=False)
    # Potential values for processing and "attatching" to a comic
    # It's very possible none of these will pan out...
    comic_name = models.CharField(max_length=255, blank=True, null=True)
    # it's far and away the most common type of numering system...
    comic_issue = models.FloatField(blank=True, null=True)
    comic_volume = models.CharField(max_length=255, blank=True, null=True)
    comic_year = models.CharField(max_length=255, blank=True, null=True)
    comic_date = models.CharField(max_length=255,  blank=True,  null=True)
    # comic_most_likely = models.ForeignKey(Comic, blank=True, null=True) ### TO DO: implement
    # Once "confirmed" these values are possible
    covers = ""  # files could have one or more covers in them! Array of keys?!
    '''
        Make a new object that's covers and use letter A - Z and numbers 1 - 100
        OR just use a general "tag" style,  with a parent|name|val setup? or just db.covers['parent', 'val']
    '''
    comic = models.ForeignKey(Comic, blank=True, null=True)
    series = models.ForeignKey(Series, blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    # ratings
    scan_quallity = models.IntegerField(blank=True, null=True)
    ads = models.BooleanField(default=True)
    # for UI filtering
    primary = models.BooleanField(default=False)
    duplicate = models.BooleanField(default=False)

    class Meta:
        unique_together = ('name', 'dir_path')

    def __unicode__(self):
        return self.name + " (" + self.dir_path + ")"


class PrimaryComics(models.Model):
    series = models.ForeignKey(Series)
    comic = models.ForeignKey(Comic)
    comicFile = models.ForeignKey(ComicFile)

    class Meta:
        unique_together = ('series', 'comic', 'comicFile')

    def __unicode__(self):
        return u"{0} | {1} | {2}".format(self.series, self.comic, self.comicFile)


class ComicReadAndOwn(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Comic)
    own = models.NullBooleanField()
    read = models.NullBooleanField()
    trade = models.NullBooleanField()

    def __unicode__(self):
        return u"{}'s {} #{}".format(self.user.username, self.issue.series.name, self.issue.number)
