from django.db import models
from django.contrib.auth.models import User
from issues.models import Series
# Create your models here.


class PullList(models.Model):
    '''
    as it's a giant has many list, it's somewhat easy to take care of...
    ...it's the information that comes out of this that becomes more important
    '''
    user = models.ForeignKey(User)
    series = models.ForeignKey(Series)

    class Meta:
        unique_together = ('user', 'series')

    def __unicode__(self):
        return self.user.username + " - " + self.series.name

    def __str__(self):
        return self.__unicode__()

    def username(self):
        return self.user.username

    def seriesname(self):
        return self.series.name
