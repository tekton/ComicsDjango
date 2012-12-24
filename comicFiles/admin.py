from django.contrib import admin
from ratings.models import UserRating
from issues.models import Series
from issues.models import Comic
from comicFiles.models import ComicFile
from comicFiles.models import RootFolder
from comicFiles import file_parsing
from django.contrib.admin.templatetags.admin_list import date_hierarchy

from comicFiles.file_parsing import parse_folder, re_parse_file

from comicFiles.images import rar_parse
from comicFiles.images import zip_parse

def folder_parse(modeladmin, request, queryset):
    #print modeladmin
    #print request
    print queryset
    for q in queryset:
        #print q
        print q.id
        parse_folder(q)

def reparse_comic(modeladmin, request, queryset):
    #print modeladmin
    #print request
    print queryset
    for q in queryset:
        #print q
        print q.id
        re_parse_file(q)    

def reparse_image(modeladmin,request,queryset):
    for q in queryset:
        if q.thumbnail is None:
            if q.extension == "cbr":
                q.thumbnail = rar_parse(q.dir_path, q.name)
            elif q.extension == "cbz":
                q.thumbnail = zip_parse(q.dir_path, q.name)
        else:
            print "Thumbnail already exist...most likely."
        q.save()

class RootFolderAdmin(admin.ModelAdmin):
    list_display = ['uri', 'last_scanned']
    ordering = ['uri','last_scanned']
    actions = [folder_parse]

class ComicFileAdmin(admin.ModelAdmin):
    list_display = ['id','name','dir_path','rootFolder']
    ordering = ['id','name','dir_path','error_flag']
    actions = [reparse_comic,reparse_image]
    list_filter = ['rootFolder','error_flag','review_flag']
    search_fields = ['name','dir_path']

folder_parse.short_description = "Parse Folder For New Comics"
reparse_comic.short_description = "ReParse the selected files"
reparse_image.short_description = "Parse thumbnail"

admin.site.register(ComicFile,ComicFileAdmin)
admin.site.register(RootFolder,RootFolderAdmin)