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
import logging

logger = logging.getLogger(__name__)


def view_by_comic_name(request, comic_name):
    comics = ComicFile.objects.filter(comic_name=comic_name).order_by("comic_issue").values()
    return render_to_response("series/possible_list.html",
                              {
                                "recentFiles": comics,
                                "comic_name": comic_name},
                              context_instance=RequestContext(request))


def makePrimary(request, series_id, comic_id, file_id):
    rtn_dict = {"success": False, "series": series_id, "comic": comic_id, "file": file_id, "primary": "null"}
    print("make primary called")
    print(rtn_dict)
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

    comicfile.primary = True
    comicfile.duplicate = False  # nuclear option to make sure we don't get in a weird state
    comicfile.comic = comic
    comicfile.series = series
    try:
        comicfile.save()
        rtn_dict["primary"] = comicfile.id
    # except IntegrityError as e:
    #     rtn_dict["success"] = False
    #     rtn_dict["primary"] = "Integrity Error"
    except Exception as e:
        rtn_dict["success"] = "False"
        rtn_dict["primary"] = '"'+str(e)+'"'

    rtn_dict["success"] = True
    logger.debug(rtn_dict)
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")


def transferPrimaries(request, series_id, unread=False):
    print("Calling transferPrimaries")
    rtn_dict = {}
    # primaries = PrimaryComics.objects.filter(series=series_id)
    primaries = ComicFile.objects.filter(primary=True, series=series_id)
    for issue in primaries:
        if unread:
            if issue.comic.read:
                rtn_dict[issue.id] = "Did not add a comic as it was already read - " + str(issue.id)
            else:
                copy_file_to_transfer.delay(issue)
                rtn_dict[issue.id] = "Adding unread comic to queue :: " + str(issue.id)
        else:
            copy_file_to_transfer.delay(issue)
            rtn_dict[issue.id] = "added to queue :: " + str(issue)
    print(rtn_dict)
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")


def api_addToDuplicates(request, series_id, comic_id, file_id):
    rtn_dict = {"success": False}
    # print("make primary called")
    # print(rtn_dict)
    try:
        comicfile = ComicFile.objects.get(pk=file_id)
        # check if primary, if so, abort!
        if comicfile.primary:
            rtn_dict["msg"] = "Can't make a primary a duplicate"
            return HttpResponse(json.dumps(rtn_dict), content_type="application/json")
    except Exception as e:
        rtn_dict["file"] = e
        return HttpResponse(json.dumps(rtn_dict), content_type="application/json")
    try:
        series = Series.objects.get(pk=series_id)
    except Exception as e:
        rtn_dict["series"] = e
        return HttpResponse(json.dumps(rtn_dict), content_type="application/json")
    try:
        comic = Comic.objects.get(pk=comic_id)
    except Exception as e:
        rtn_dict["comic"] = e
        return HttpResponse(json.dumps(rtn_dict), content_type="application/json")

    comicfile.duplicate = True
    comicfile.comic = comic
    comicfile.series = series
    try:
        comicfile.save()
        rtn_dict["duplicate"] = comicfile.id
    # except IntegrityError as e:
    #     rtn_dict["success"] = False
    #     rtn_dict["primary"] = "Integrity Error"
    except Exception as e:
        rtn_dict["duplicate"] = '"'+str(e)+'"'

    rtn_dict["success"] = True
    logger.debug(rtn_dict)
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")
    # remove entry from main archive and save to "duplicates" table
    # move the file to a different folder, update the DB
