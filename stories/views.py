from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.conf import settings
from django.db.models import *

from collections import OrderedDict

import json

#from forms import *
from issues.models import *
from stories.models import *
#from comicFiles.models import *
#from PullLists.models import *
#from ratings.models import *



# Create your views here.

def addIssueToStory(request,arc,comic):
    '''Handle AJAX adds'''
    pass

def viewArcAJAX(request,arc):
    '''Handle AJAX views'''
    pass


def getSeriesList(request):
    '''
    
        AJAX :: handle series request
        Possibly not needed as it's really easier to just have this pulled at the begining
    
    '''
    series = Series.objects.all().values()
    return HttpResponse(json.dumps(list(series)), mimetype="application/json")

def getComicsFromSeries(request,series):
    '''
    
        AJAX :: handle issues request based on series
    
        possible way to populate drop down:
        --check for series.change
        var list = $('#items')[0]; // HTMLSelectElement
        $.each(numbers, function(index, text) { 
            list.options[list.options.length] = new Option(index, text);
        });
    
    '''
    comics = Comic.objects.filter(series=series).values()
    return HttpResponse(json.dumps(list(comics)), mimetype="application/json")
