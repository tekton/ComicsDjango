from django.db import models
from issues.models import Comic
from django.contrib.auth.models import User

# Create your models here.
class user_rating(models.Model):
    user = models.ForeignKey(User)
    comic = models.ForeignKey(Comic)
    