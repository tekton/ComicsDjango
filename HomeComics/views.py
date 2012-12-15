from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from collections import OrderedDict

from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

# Create your views here.

def index(request):
	recentFiles = ComicFile.objects.all()[:5].values()
	
	print ComicFile.objects.filter(extension__contains='cbz').count()
	print ComicFile.objects.filter(extension__contains='cbr').count()
	
	return render_to_response("index.html", {"recentFiles":recentFiles}, context_instance=RequestContext(request))

def single_issue(request,id):
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
	pass