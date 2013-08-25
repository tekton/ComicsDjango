import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import *

from issues.models import Series
from models import PullList

def addToPullList(request, series_id):
    rtn_dict = {}
    try:
        series = Series.objects.get(pk=series_id)
        rtn_dict["success"] = True
    except Exception as e:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Series doesn't exist"
        rtn_dict["e"] = str(e)
    if series:
        pull = PullList()
        pull.user = request.user
        pull.series = series
    try:
        pull.save()
    except Exception as e:
        rtn_dict["success"] = False
        rtn_dict["error"] = "Unable to save pull list"
        rtn_dict["e"] = str(e)        
    return HttpResponse(json.dumps(rtn_dict), mimetype="application/json")
