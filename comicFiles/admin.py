from django.contrib import admin
from ratings.models import UserRating
from issues.models import Series
from issues.models import Comic
from comicFiles.models import ComicFile
from comicFiles.models import RootFolder
from comicFiles import file_parsing
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from comicFiles.file_parsing import parse_folder

def folder_parse(modeladmin, request, queryset):
    #print modeladmin
    #print request
    print queryset
    for q in queryset:
        #print q
        parse_folder(q)

class RootFolderAdmin(admin.ModelAdmin):
    list_display = ['uri', 'last_scanned']
    ordering = ['uri','last_scanned']
    actions = [folder_parse]

folder_parse.short_description = "Parse Folder For New Comics"
admin.site.register(ComicFile)
admin.site.register(RootFolder,RootFolderAdmin)