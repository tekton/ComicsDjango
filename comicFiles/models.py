from django.db import models
from issues.models import Comic

# Create your models here.
    
class RootFolder(models.Model):
    uri = models.CharField(max_length=255)
    last_scanned = models.DateTimeField(blank=True,null=True)
    
class ComicFile(models.Model):
    ### The one things they'll all have
    name = models.CharField(max_length=255)
    ### Should have, but in case they're not needed for some reason...
    folder = models.ForeignKey(RootFolder,blank=True,null=True)
    extension = models.CharField(max_length=255,blank=True,null=True)
    ### Parsing potential...
    error_flag = models.BooleanField(default=False)
    review_flag = models.BooleanField(default=False)
    ### Potential values for processing and "attatching" to a comic
    ### It's very possible none of these will pan out...
    comic_name = models.CharField(max_length=255,blank=True,null=True)
    comic_issue = models.CharField(max_length=255,blank=True,null=True)
    comic_volume = models.CharField(max_length=255,blank=True,null=True)
    comic_year = models.CharField(max_length=255,blank=True,null=True)
    comic_most_likely = models.ForeignKey(Comic,blank=True,null=True)
    ### Once "confirmed" these values are possible
    covers = "" #files could have one or more covers in them! Array of keys?! 
    '''
        Make a new object that's covers and use letter A - Z and numbers 1 - 100
        OR just use a general "tag" style, with a parent|name|val setup? or just db.covers['parent','val']
    '''
    comic = models.ForeignKey(Comic,blank=True,null=True)