from django.db import models
from issues.models import Series,Comic

# Create your models here.

class StoryArc(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name   
    

class StoryArcIssue(models.Model):
    storyarc = models.ForeignKey(StoryArc)
    issue = models.ForeignKey(Comic)
    order = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.storyarc) + " " + str(self.order)
    
