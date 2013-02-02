from django.db import models
from issues.models import Comic
from django.contrib.auth.models import User


class UserRating(models.Model):
    user = models.ForeignKey(User)
    comic = models.ForeignKey(Comic)
    overall = models.IntegerField(blank=True, null=True)
    art = models.IntegerField(blank=True, null=True)
    story = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username + " - " + self.comic.name
