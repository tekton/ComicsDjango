from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from collections import OrderedDict
from django.db.models import *

from HomeComics.forms import *
from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

from django.conf import settings

def search_all(request):
    form = SearchFormClass()
    try:
        form = SearchFormClass(request.POST)
        srch_str = form.data["search_data"]
        #print srch_str
        files = ComicFile.objects.filter(name__icontains=srch_str).values()
        file_by_dir = ComicFile.objects.filter(dir_path__icontains=srch_str).values()
        comics = Comic.objects.filter(name__icontains=srch_str).values()
        series = Series.objects.filter(name__icontains=srch_str)#.values()
        print file_by_dir.query
        #print files.query
        #print comics.query
        #print series.query
    except:
        form = SearchFormClass()
    if form.is_valid:
        pass
    else:
        print "Invalid form!"
        pass
        ###show blank form again!
    
    return render_to_response("search.html", {"form":form,"seri":series,"files":files,"comics":comics,"file_by_dir":file_by_dir}, context_instance=RequestContext(request))
    