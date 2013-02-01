from django.db import models
from django.contrib.auth.models import User
from issues.models import Comic


class HomeComic(models.Model):
    user = models.ForeignKey(User)
    comic = models.ForeignKey(Comic)
    cover = models.CharField(max_length=255, blank=True, null=True)
    box = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.user.username + "'s " + self.comic.name
