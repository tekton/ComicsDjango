from django.contrib import admin
from ratings.models import UserRating
from issues.models import Series
from issues.models import Comic
from comicFiles.models import ComicFile
from comicFiles.models import RootFolder
from comicFiles.models import TransferRoot, PrimaryComics
from comicFiles import file_parsing
from django.contrib.admin.templatetags.admin_list import date_hierarchy

from comicFiles.file_parsing import parse_folder, re_parse_file,copy_file_to_transfer

from comicFiles.images import rar_parse,zip_parse,thumbnail_parse_task


def folder_parse(modeladmin, request, queryset):
    #print modeladmin
    #print request
    print queryset
    for q in queryset:
        #print q
        print q.id
        parse_folder.delay(q)


def reparse_comic(modeladmin, request, queryset):
    #print modeladmin
    #print request
    print queryset
    for q in queryset:
        #print q
        print q.id
        re_parse_file.delay(q)


def reparse_image(modeladmin, request, queryset):
    for q in queryset:
        thumbnail_parse_task.delay(q)


def copy_to_transfer(modeladmin, request, queryset):
    for q in queryset:
        copy_file_to_transfer.delay(q)


class RootFolderAdmin(admin.ModelAdmin):
    list_display = ['uri', 'last_scanned']
    ordering = ['uri', 'last_scanned']
    actions = [folder_parse]


class ComicFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dir_path', 'rootFolder', 'comic_issue']
    ordering = ['id', 'name', 'dir_path', 'error_flag']
    actions = [reparse_comic, reparse_image, copy_to_transfer]
    list_filter = ['rootFolder', 'error_flag', 'review_flag']
    search_fields = ['name', 'dir_path', 'comic_issue', 'comic_name']

folder_parse.short_description = "Parse Folder For New Comics"
reparse_comic.short_description = "ReParse the selected files"
reparse_image.short_description = "Parse thumbnail"
copy_to_transfer.short_description = "Copy to Primary Transfer"

admin.site.register(ComicFile, ComicFileAdmin)
admin.site.register(RootFolder, RootFolderAdmin)
admin.site.register(TransferRoot)
admin.site.register(PrimaryComics)

