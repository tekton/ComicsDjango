from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from collections import OrderedDict

from forms import *
from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

from django.conf import settings

# Create your views here.

def index(request):
    recentFiles = ComicFile.objects.all().order_by("-id")[:5].values()
    
    #recentFiles = ComicFile.objects.filter(rootFolder=3).values()
    
    print ComicFile.objects.filter(extension__contains='cbz').count()
    print ComicFile.objects.filter(extension__contains='cbr').count()
    #
    print settings.IMG_ROOT
    #
    return render_to_response("index.html", {"recentFiles":recentFiles}, context_instance=RequestContext(request))

def single_issue(request,id):
    print "SINGLE ISSUE"
    comic = ComicFile.objects.get(pk=id)
    return render_to_response("single_issue.html", {"comic":comic}, context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST':
        ### construct the query!
        '''
            for each set of fields take the: column,value and add it as a filter!
        '''
        ### return a response to show what was found!
        return render_to_response("search.html", context_instance=RequestContext(request))
    else:
        ### display the search form!
        return render_to_response("search.html", context_instance=RequestContext(request))
    
def issue_search_issue(request,series,volume,number):
    comics = ComicFile.objects.all().order_by("-id")[:50].values()
    return render_to_response("files_recent_by_id.html", {"recentFiles":comics}, context_instance=RequestContext(request))
    
def recent_by_id(request):
    comics = ComicFile.objects.all().order_by("-id")[:50].values()
    return render_to_response("files_recent_by_id.html", {"recentFiles":comics}, context_instance=RequestContext(request))

def new_series_from_data(request,id):
    comic = ComicFile.objects.get(pk=id)
    if request.POST:
        print "posting..."
        form = NewSeriesFromData(request.POST)
        if form.is_valid():
            print "valid form is valid!"
            print form.data["series"]
            print form.data["max_issue"]
            try:
                series = Series.objects.get(name=form.data["series"])
                print "Series already exists...should try to increase to new number!"
            except Series.DoesNotExist:
                series = Series(name=form.data["series"])
                series.save()
                print "No series yet!"
            except:
                print "um...what?!"
            #try:
            try:
                min_num = int(form.data["min_issue"])
                max_num = int(form.data["max_issue"])
                rng = True
            except:
                rng = False
            if rng:
                for x in range(min_num, max_num):
                    #print x
                    try:
                        issue = Comic.objects.get(series=series,number=x)
                        print "Issue exists!"
                    except Comic.DoesNotExist:
                        print "should create a new issue..."
                        issue = Comic(series=series,number=x)
                        issue.save()
            else:
                print "something wrong with range; just check/create a single entry..."
                try:
                    issue = Comic.objects.get(series=series,number=comic.comic_issue)
                    print "It exists anyway..."
                except Comic.DoesNotExist:
                    issue = Comic(series=series,number=comic.comic_issue)
                    issue.save()
                    print "New entry created!"
            #except:
            #    print "just create a single issue in the series based on the current book..."
            
    else:
        form = NewSeriesFromData()
        form.initial['orig_id'] = id
        form.initial['series'] = comic.comic_name
        form.initial['max_issue'] = int(comic.comic_issue)
    
        min_issue = int(comic.comic_issue) - 50
        if min_issue < 0:
            min_issue = 0
    
        form.initial['min_issue'] = min_issue
    return render_to_response("create_series_from_book.html", {"form":form,"comic":comic}, context_instance=RequestContext(request))

def new_series_form(request):    
    comics = ComicFile.objects.all().order_by("-id")[:50].values()
    return render_to_response("files_recent_by_id.html", {"recentFiles":comics}, context_instance=RequestContext(request))
