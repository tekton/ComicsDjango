from django.db import models
from issues.models import Comic

# Create your models here.

class ComicFile(models.Model):
    covers = "" #files could have one or more covers in them!
    comic = models.ForeignKey(Comic)