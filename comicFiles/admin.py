from django.contrib import admin
from ratings.models import UserRating
from issues.models import Series
from issues.models import Comic
from comicFiles.models import ComicFile
from django.contrib.admin.templatetags.admin_list import date_hierarchy

#class ComicFileAdmin(admin.ModelAdmin):
    
admin.site.register(ComicFile)