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
def index(request):
    series_list = Series.objects.all()
    return render_to_response("series/index.html", {"series_list":series_list}, context_instance=RequestContext(request))
    
def browse(request,id):
    print "browse"
    series = Series.objects.get(pk=id)
    issues = Comic.objects.filter(series=series)
    return render_to_response("series/browse.html", {"series":series,"comics":issues}, context_instance=RequestContext(request))