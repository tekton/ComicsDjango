from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *


import json

from issues.models import *
from stories.models import *


def newArcDisplay(request):
    ### if post

    ### else

    #return

    return render_to_response("arc/form.html", {}, context_instance=RequestContext(request))


def addIssueToStory(request, arc, comic):
    '''

        Handle AJAX adds

        What I *want* to happen:
            if this returns success, make the row it came from un-editable
            add new row with a blank series dropdown, or the same one as before
    '''
    pass


def viewArcAJAX(request, arc):
    '''Handle AJAX views'''
    pass


def getSeriesList(request):
    '''
        AJAX :: handle series request
        Possibly not needed as it's really easier to just have this pulled at the begining
    '''
    series = Series.objects.all().values()
    return HttpResponse(json.dumps(list(series)), mimetype="application/json")


def getComicsFromSeries(request, series):
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
