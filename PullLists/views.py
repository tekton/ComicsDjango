import json

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *

from Comics import json_encoder

from issues.models import Series, Comic
from comicFiles.models import PrimaryComics, ComicReadAndOwn
from PullLists.models import PullList

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
        rtn_dict["success"] = True
        for pull in pulllist:  # this sadly can cause a lot of db hits; should probably sync this up in redis instead...
            primaries = PrimaryComics.objects.filter(series=pull.series.id)
            for item in primaries:
                rtn_dict[item.series.name][item.comic.number] = {"name": item.comic.name,
                                                                 "image": item.comicFile.thumbnail,
                                                                 }
    else:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Unable to get pull list for user"
    #
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")


def currentList(request):
    pulllist = PullList.objects.filter(user=request.user)  # .order_by('series')
    return render_to_response("pulllist/index.html",
                              {"series_list": pulllist},
                              context_instance=RequestContext(request))


def api_current_list(request):
    pulllist = PullList.objects.filter(user=request.user).values("series__name", "id", "series")
    rtn_list = json_encoder.serialize_to_json(pulllist)
    return HttpResponse(rtn_list, content_type="application/json")


def deleteList(request, pl_id):
    #
    try:
        PullList.objects.get(pk=pl_id).delete()
    except Exception as e:
        print(e)
    # return redirect('PullList.views.currentList')
    return redirect('/pull')
    # return render_to_response("pulllist/index.html", {"series_list": pulllist}, context_instance=RequestContext(request))


def ownedSeriesList(request):
    serieses = ComicReadAndOwn.objects.filter(user=request.user).values("issue__series__name").annotate(c=Count("issue__series__name"))
    print(serieses)
    rtn_dict = defaultdict(dict)
    for series in serieses:
        rtn_dict[series["issue__series__name"]] = series["c"]
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")


def missing(request):
    serieses = ComicReadAndOwn.objects.filter(user=request.user).values("issue__series__name").annotate(c=Count("issue__series__name"))
    rtn_dict = defaultdict(list)
    for series in serieses:
        # rtn_dict[series["issue__series__name"]] = series["c"]
        sereies_to_check = Comic.objects.filter(series__name=series["issue__series__name"])
        for x in sereies_to_check:
            rtn_dict[series["issue__series__name"]].append(x.number)
        owned = ComicReadAndOwn.objects.filter(issue__series__name=series["issue__series__name"])
        for own in owned:
            rtn_dict[series["issue__series__name"]] = filter(lambda a: a != own.issue.number, rtn_dict[series["issue__series__name"]])
    print(rtn_dict)
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")