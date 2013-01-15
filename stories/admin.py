from django.contrib import admin
from models import *
from django.contrib.admin.templatetags.admin_list import date_hierarchy

#class ComicFileAdmin(admin.ModelAdmin):

admin.site.register(StoryArc)
admin.site.register(StoryArcIssue)