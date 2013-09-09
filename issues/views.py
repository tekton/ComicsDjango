from django.shortcuts import render_to_response, redirect
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
    # print possible
    return render_to_response("series/single.html", {"comic": comic, "possible": possible}, context_instance=RequestContext(request))


def browse(request, id):
    # print "browse"
    series = Series.objects.get(pk=id)
    # issues = Comic.objects.filter(series=series).order_by("-number")  # V1
    # connection = (Comic._meta.db_table, ComicReadAndOwn._meta.db_table, "id", "issue_id")
    '''issues = Comic.objects.filter(series=series).order_by("-number").extra(select={"read": "comicFiles_comicreadandown.read",
                                                                                   "own": "comicFiles_comicreadandown.own"},
                                                                           where=["(comicFiles_comicreadandown.user_id = %s OR comicFiles_comicreadandown.user_id IS NULL)"],
                                                                           params=[request.user.id]);
    '''
    # issues.query.join(connection,promote=True)
    # issues = Comic.objects.raw("select * from issues_comic where series_id = %s order by number+0 desc",[series.id])###
    # print issues

    issues = Comic.objects.raw('''
        SELECT  (comicFiles_comicreadandown.read) AS `read`,
                (comicFiles_comicreadandown.own) AS `own`,
                `issues_comic`.`id`, `issues_comic`.`name`,
                `issues_comic`.`number`,
                `issues_comic`.`year`,
                `issues_comic`.`series_id`,
                `issues_comic`.`annual`,
                `issues_comic`.`annual_number`
                FROM `issues_comic` 
                LEFT OUTER JOIN `comicFiles_comicreadandown`
                ON (`issues_comic`.`id` = `comicFiles_comicreadandown`.`issue_id` AND 
                    comicFiles_comicreadandown.user_id = %s) 
                WHERE (`issues_comic`.`series_id` = %s);
        ''',[request.user.id, series.id])
    print issues.query
    return render_to_response("series/browse.html", {"series": series, "comics": issues}, context_instance=RequestContext(request))


def browseUnread(request, id):
    # print "browse"
    series = Series.objects.get(pk=id)
    issues = Comic.objects.filter(series=series, primary=True, read=False).order_by("-number")
    # issues = Comic.objects.raw("select * from issues_comic where series_id = %s order by number+0 desc",[series.id])###
    # print issues
    return render_to_response("series/browse.html", {"series": series, "comics": issues}, context_instance=RequestContext(request))


def incrementSeries(request, series_id):
    try:
        series = Series.objects.get(pk=series_id)
    except:
        print "Unable to find series..."
        return redirect('issues.views.browse', series_id)
    max_comic = Comic.objects.filter(series=series).aggregate(Max('number'))
    # check the +1 comic for being beyond the series max
    max_num = int(max_comic["number__max"]) + 1

    print str(series.series_max), str(max_comic), str(max_num)

    if series.series_max is not None:
        if int(max_num) > int(series.series_max):
            print "New max is over the series max"
            return redirect('issues.views.browse', series_id)
        else:
            pass
    else:
        pass
    issue = Comic(series=series, number=max_num)
    issue.save()
    return redirect('issues.views.browse', series_id)


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
        # print issue
    except Exception as e:
        rtn_dict["goc_error"] = "Unable to get or create set"
        rtn_dict["get_error"] = str(e)
        # print e
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
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
