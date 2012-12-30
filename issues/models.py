from django.db import models

# Create your models here.


class Series(models.Model):
	'''
	To really keep track of things, every book needs to be part of a series; 
	the hard part is going to be graphic novels but those should be their own model type with a list of series/issues
	'''
	name = models.CharField(max_length=255)
	volume = models.CharField(max_length=255,blank=True,null=True)
	mini_series_flag = models.BooleanField(default=False)
	series_max = models.CharField(max_length=255,blank=True,null=True) ## useful for old series and mini series, a la Flashpoint
	publisher = models.CharField(max_length=255,blank=True,null=True) ### could turn in to a select given how few there really are
	new52_flag = models.BooleanField(default=False)
	marvel_now = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name + " v" + self.volume

class Comic(models.Model):
	'''
		this class is for the actual issues/series management side of things
	'''
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=255)  ###ususally numbers, but there's a decent amount of A, B, C, 50.1, etc
	year = models.CharField(max_length=255,blank=True,null=True) ###should be a date or year stamp
	series = models.ForeignKey(Series)
	read = models.BooleanField(default=False)
	own = models.BooleanField(default=False)
	def __unicode__(self):
		rtn_str = self.series.name + " v" + self.series.volume + " " + self.number
		if self.series.new52_flag == True:
			rtn_str += " (New 52)"
		if self.series.marvel_now == True:
			rtn_str += "(Marvel NOW!)"
		return rtn_str


#### Other custom code

	
#### THESE SHOULD GO IN THERE OWN APPS

