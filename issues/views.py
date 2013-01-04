from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from collections import OrderedDict
from django.db.models import *

#from forms import *
from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

from django.conf import settings

import json

# Create your views here.
def index(request):
    series_list = Series.objects.all()
    return render_to_response("series/index.html", {"series_list":series_list}, context_instance=RequestContext(request))

def single(request,id):
    comic = Comic.objects.get(pk=id)
    return render_to_response("series/single.html", {"comic":comic}, context_instance=RequestContext(request))
    
def browse(request,id):
    print "browse"
    series = Series.objects.get(pk=id)
    issues = Comic.objects.filter(series=series).order_by("number")
    return render_to_response("series/browse.html", {"series":series,"comics":issues}, context_instance=RequestContext(request))
    

def toggle_box(request,id,box):
    print id,box
    
    rtn_dict = {"Success":"failure",box:"untouched"}
    
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