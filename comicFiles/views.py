from django.shortcuts import render_to_response
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
# Create your views here.

def view_by_comic_name(request,comic_name):
    comics = ComicFile.objects.filter(comic_name=comic_name).order_by("comic_issue").values()
    #return render_to_response("comicFiles/comic_name_list.html", {"comics":comics}, context_instance=RequestContext(request))
    return render_to_response("files_recent_by_id.html", {"recentFiles":comics}, context_instance=RequestContext(request))
    
#@depricated
def CreateSeriesFromIssue(comic):
    """Moved to issues"""
    series = Series()
    return