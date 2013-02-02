from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *

from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

import json


def index(request):
    series_list = Series.objects.all()
    return render_to_response("series/index.html", {"series_list": series_list}, context_instance=RequestContext(request))


def single(request, id):
    comic = Comic.objects.get(pk=id)
    possible = ComicFile.objects.filter(comic_name=comic.series.name, comic_issue=comic.number).values()
    print possible
    return render_to_response("series/single.html", {"comic": comic, "possible": possible}, context_instance=RequestContext(request))


def browse(request, id):
    print "browse"
    series = Series.objects.get(pk=id)
    issues = Comic.objects.filter(series=series).order_by("-number")
    #issues = Comic.objects.raw("select * from issues_comic where series_id = %s order by number+0 desc",[series.id])###
    print issues
    return render_to_response("series/browse.html", {"series": series, "comics": issues}, context_instance=RequestContext(request))


def toggle_box(request, id, box):
    print id, box

    rtn_dict = {"Success": "failure", box: "untouched"}

    try:
        issue = Comic.objects.get(pk=id)
        print issue
    except:
        rtn_dict["Success"] = "No comic!"

    if box == "own":
        if issue.own is True:
            issue.own = False
            rtn_dict[box] = "False"
        else:
            issue.own = True
            rtn_dict[box] = "True"
    elif box == "read":
        if issue.read is True:
            issue.read = False
            rtn_dict[box] = "False"
        else:
            issue.read = True
            rtn_dict[box] = "True"
    else:
        rtn_dict["Success"] = "Invalid box type sent"

    try:
        issue.save()
        print "Saved!"
        print issue
    except:
        rtn_dict["Success"] = "Unable to save"

    rtn_dict["Success"] = "Updated!"
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
