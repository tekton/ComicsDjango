from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *
import datetime
import requests
import logging
import operator

from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

import json

logger = logging.getLogger(__name__)


def index(request):
    series_list = Series.objects.all()
    return render_to_response("series/index.html",
                              {"series_list": series_list},
                              context_instance=RequestContext(request))


def single(request, id):
    comic = Comic.objects.get(pk=id)
    possible = ComicFile.objects.filter(comic_name=comic.series.name, comic_issue=comic.number).values()
    return render_to_response("series/single.html",
                              {"comic": comic, "possible": possible},
                              context_instance=RequestContext(request))


def browse(request, id):
    # print("browse")
    print(id)
    series = Series.objects.get(pk=id)
    issues = Comic.objects.raw('''
        SELECT  (comicFiles_comicreadandown.read) AS `read`,
                (comicFiles_comicreadandown.own) AS `own`,
                `issues_comic`.`id`, `issues_comic`.`name`,
                `issues_comic`.`number`,
                `issues_comic`.`year`,
                `issues_comic`.`series_id`,
                `issues_comic`.`annual`,
                `issues_comic`.`annual_number`,
                (ratings_userrating.art) as `art`,
                (ratings_userrating.story) as `story`,
                (ratings_userrating.overall) as `overall`
                FROM `issues_comic`
                LEFT OUTER JOIN `comicFiles_comicreadandown`
                ON (`issues_comic`.`id` = `comicFiles_comicreadandown`.`issue_id` AND
                    comicFiles_comicreadandown.user_id = %s)
                LEFT OUTER JOIN `ratings_userrating`
                ON (`issues_comic`.`id` = `ratings_userrating`.`comic_id` AND
                    ratings_userrating.user_id = %s)
                WHERE (`issues_comic`.`series_id` = %s);
        ''', [request.user.id, request.user.id, series.id])
    # print(issues.query)
    return render_to_response("series/browse.html",
                              {"series": series,
                               "comics": issues},
                              context_instance=RequestContext(request))


def browseUnread(request, id):
    # print("browse")
    series = Series.objects.get(pk=id)
    issues = Comic.objects.filter(series=series, primary=True, read=False).order_by("-number")
    # issues = Comic.objects.raw("select * from issues_comic where series_id = %s order by number+0 desc",[series.id])##
    # print(issues)
    return render_to_response("series/browse.html",
                              {
                                "series": series,
                                "comics": issues
                              }, context_instance=RequestContext(request))


def incrementSeries(request, series_id):
    max_num = 1

    try:
        series = Series.objects.get(pk=series_id)
    except:
        print("Unable to find series...")
        return redirect('issues:browse', series_id)
    max_comic = Comic.objects.filter(series=series).aggregate(Max('number'))
    # check the +1 comic for being beyond the series max
    if max_comic["number__max"] is not None:
        max_num = int(max_comic["number__max"]) + 1

    print("{} :: {} :: {}".format(str(series.series_max), str(max_comic), str(max_num)))

    if series.series_max is not None and series.series_max != '':
        if int(max_num) > int(series.series_max):
            print("New max is over the series max")
            return redirect('issues:browse', series_id)
        else:
            pass
    else:
        pass
    issue = Comic(series=series, number=max_num)
    issue.save()
    return redirect('issues:browse', series_id)


def toggle_box(request, comic_id, box):
    rtn_dict = {"Success": "failure", box: "untouched"}
    issue = False
    try:
        comic = Comic.objects.get(pk=comic_id)
    except Exception as e:
        rtn_dict["comic_error"] = "Unable to get comic"
        rtn_dict["get_error"] = str(e)

    try:
        issue, created = ComicReadAndOwn.objects.get_or_create(issue=comic, user=request.user)
        # print(issue)
    except Exception as e:
        rtn_dict["goc_error"] = "Unable to get or create set"
        rtn_dict["get_error"] = str(e)
        # print(e)
    if issue:
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
        except Exception as e:
            rtn_dict["Success"] = "Unable to save"
            rtn_dict["save_error"] = str(e)

        rtn_dict["Success"] = "Updated!"
    else:
        rtn_dict["Success"] = "False"
        rtn_dict["error"] = "Issue not obtained"
    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")


def cv_results_by_year(res, name):
    rtn_list = []
    for itm in res:
        if itm["name"] == name:
            rtn_list.append({"id": [itm["id"]],
                             "name": itm["name"],
                             "start_year": itm["start_year"]})
            print(itm["name"], itm["id"], itm["start_year"])
    print(rtn_list)
    return rtn_list


def possible_series_list_by_date(series_name=None, pub_year=None, pub_month=None, data=None):
    if not data or not series_name:
        return False
    if not pub_year:
        pub_year = datetime.datetime.now().year
    if not pub_month:
        pub_month = datetime.datetime.now().month
    pub_year = int(pub_year)  # Just make sure, just in case...
    year_list = cv_results_by_year(data["results"], series_name)
    # remove all the items that are "after" the current pub_year
    year_list[:] = [x for x in year_list if int(x["start_year"]) <= pub_year]
    # compute the difference for all other returns
    for itm in year_list:
        itm["diff"] = pub_year - int(itm["start_year"])
    # sort the list by the differences
    year_list.sort(key=operator.itemgetter("diff"))
    # get the nearest diff, then remove all other
    diff = year_list[0]["diff"]
    year_list[:] = [x for x in year_list if not x["diff"] > diff]
    # if two come out as viable candidates, then go in and investiagte them further for issue dates...
    if len(year_list) > 1:
        print("More than one...")
    else:
        print(year_list)


def cv_api_request(url):
    try:
        r = requests.get(url)
        return r
    except Exception as e:
        logger.error(e)


def construct_cv_url(url_dict):
    if "ids" in url_dict:
        if url_dict["ids"]:
            url = "http://www.comicvine.com/api/{}/{}/".format(url_dict["type"], url_dict["ids"])
        else:
            url = "http://www.comicvine.com/api/{}/".format(url_dict["type"])
    if "qs" in url_dict:
        if url_dict["qs"]:
            url += "?"
            for key in url_dict["qs"]:
                url += "&{}={}".format(key, url_dict["qs"][key])
    return url


def api_volumes_get_search_comicvine(volume_name=None, api_type="search"):
    if not settings.COMICVINE_API_KEY:
        return False
    url_dict = {
        "qs": {
            "resources": "volume",
            "query": volume_name,
            "format": "json",
            "api_key": settings.COMICVINE_API_KEY,
        },
        "type": api_type,
        "ids": None,
    }
    # construct URL
    url = construct_cv_url(url_dict)
    # print(url)
    # make call...
    res = cv_api_request(url)
    return res
