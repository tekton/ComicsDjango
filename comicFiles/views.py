from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *

from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

from comicFiles.file_parsing import copy_file_to_transfer

import json

#from django.conf import settings
#from django.http import HttpResponseRedirect
#from django.http import Http404
#from collections import OrderedDict
#from forms import *
# Create your views here.


def view_by_comic_name(request, comic_name):
    comics = ComicFile.objects.filter(comic_name=comic_name).order_by("comic_issue").values()
    #return render_to_response("comicFiles/comic_name_list.html", {"comics":comics}, context_instance=RequestContext(request))
    return render_to_response("files_recent_by_id.html", {"recentFiles": comics}, context_instance=RequestContext(request))


def makePrimary(request, series_id, comic_id, file_id):
    rtn_dict = {"success": "True", "series": series_id, "comic": comic_id, "file": file_id, "primary": "null"}
    print "make primary called"
    print rtn_dict
    try:
        series = Series.objects.get(pk=series_id)
    except Exception as e:
        rtn_dict["success"] = "False"
        rtn_dict["series"] = e
    try:
        comic = Comic.objects.get(pk=comic_id)
    except Exception as e:
        rtn_dict["success"] = "False"
        rtn_dict["comic"] = e
    try:
        comicfile = ComicFile.objects.get(pk=file_id)
    except Exception as e:
        rtn_dict["success"] = "False"
        rtn_dict["file"] = e

    primary = PrimaryComics()
    primary.series = series
    primary.comic = comic
    primary.comicFile = comicfile
    try:
        primary.save()
        rtn_dict["primary"] = primary.id
    # except IntegrityError as e:
    #     rtn_dict["success"] = False
    #     rtn_dict["primary"] = "Integrity Error"
    except Exception as e:
        rtn_dict["success"] = "False"
        rtn_dict["primary"] = '"'+str(e)+'"'

    print rtn_dict

    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")

def transferPrimaries(request, series_id, unread=False):
    print "Calling transferPrimaries"
    rtn_dict = {}
    primaries = PrimaryComics.objects.filter(series=series_id)
    for issue in primaries:
        if unread:
            if issue.comic.read:
                rtn_dict[issue.id] = "Did not add a comic as it was already read - " + str(issue.comicFile.id)
            else:
                copy_file_to_transfer.delay(issue.comicFile.id)
                rtn_dict[issue.id] = "Adding unread comic to queue :: " + str(issue.comicFile.id)
        else:
            copy_file_to_transfer.delay(issue.comicFile.id)
            rtn_dict[issue.id] = "added to queue :: " + str(issue.comicFile.id)
    print rtn_dict
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
