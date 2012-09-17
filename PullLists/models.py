from django.db import models
from django.contrib.auth.models import User
from issues.models import Series
# Create your models here.

'''
	as it's a giant has many list, it's somewhat easy to take care of...
	...it's the information that comes out of this that becomes more important
'''
class PullList(models.Model):
	user = models.ForeignKey(User)
	series = models.ForeignKey(Series)
	def __unicode__(self):
		return self.user.username + " - " + self.series.name
	def username(self):
		return self.user.username
	def seriesname(self):
		return self.series.name
#### Other custom code

	
#### THESE SHOULD GO IN THERE OWN APPS

