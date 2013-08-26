import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import *

from issues.models import Series
from comicFiles.models import PrimaryComics
from models import PullList

from collections import defaultdict

def addToPullList(request, series_id):
    rtn_dict = {}
    try:
        series = Series.objects.get(pk=series_id)
        rtn_dict["success"] = True
    except Exception as e:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Series doesn't exist"
        rtn_dict["e"] = str(e)
    if series:
        pull = PullList()
        pull.user = request.user
        pull.series = series
    try:
        pull.save()
    except Exception as e:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Unable to save pull list"
        rtn_dict["e"] = str(e)        
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")


def recentPullListCovers(request):
    # rtn_dict = {}
    rtn_dict = defaultdict(dict)
    # get users pull list info...
    pulllist = PullList.objects.filter(user=request.user)
    if pulllist:
        pass
    else:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Unable to get pull list for user"
        return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
        #
    for pull in pulllist:
        primaries = PrimaryComics.objects.filter(series=pull.series.id)
        for item in primaries:
            rtn_dict[item.series.name][item.comic.number] = {"name": item.comic.name, "image": item.comicFile.thumbnail}
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
