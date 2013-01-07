from django.db import models

# Create your models here.

'''
    To really keep track of things, every book needs to be part of a series; 
    the hard part is going to be graphic novels but those should be their own model type with a list of series/issues
'''
class Series(models.Model):
    name = models.CharField(max_length=255)
    volume = models.CharField(max_length=255,blank=True,null=True)
    mini_series_flag = models.BooleanField(default=False)
    series_max = models.CharField(max_length=255,blank=True,null=True) ## useful for old series and mini series, a la Flashpoint
    publisher = models.CharField(max_length=255,blank=True,null=True) ### could turn in to a select given how few there really are
    new52_flag = models.BooleanField(default=False)
    marvel_now = models.BooleanField(default=False)
    def __unicode__(self):
        if self.volume:
            v_str = " v" + str(self.volume)
        else:
            v_str = ""
  
        rtn_str = str(self.name) + v_str
        if self.new52_flag == True:
            rtn_str += " (New 52)"
        if self.marvel_now == True:
            rtn_str += "(Marvel NOW!)"
        return rtn_str
'''
    this class is for the actual issues/series management side of things
'''
class Comic(models.Model):
    name = models.CharField(max_length=255)
    number = models.FloatField()  ###ususally numbers, but there's a decent amount of A, B, C, etc
    year = models.CharField(max_length=255,blank=True,null=True) ###should be a date or year stamp
    series = models.ForeignKey(Series)
    read = models.BooleanField(default=False)
    own = models.BooleanField(default=False)
    def __unicode__(self):
        rtn_str = str(self.series.name) + " " + str(self.number)
        if self.series.new52_flag == True:
            rtn_str += " (New 52)"
        if self.series.marvel_now == True:
            rtn_str += "(Marvel NOW!)"
        return rtn_str


#### Other custom code

    
#### THESE SHOULD GO IN THERE OWN APPS

