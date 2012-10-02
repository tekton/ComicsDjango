from django.contrib import admin
from ratings.models import UserRating
from issues.models import Series
from issues.models import Comic
from comicFiles.models import ComicFile
from django.contrib.admin.templatetags.admin_list import date_hierarchy

#class ComicFileAdmin(admin.ModelAdmin):

def make_new52(modeladmin, request, queryset):
    queryset.update(new52_flag=True)
make_new52.short_description = "Make part of New 52"

class ComicInline(admin.TabularInline):
    model = Comic

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher', 'new52_flag']
    ordering = ['name']
    inlines = [ComicInline]
    actions = [make_new52]

admin.site.register(Series, SeriesAdmin)
admin.site.register(Comic)