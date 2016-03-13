from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import *

from comicFiles.models import *
from issues.models import *
from PullLists.models import *
from ratings.models import *

import json

# Create your views here.

def set_user_rating(request, issue_id, category, val):
    rtn_dict = {"success": False, "issue": issue_id, "category": category, "score": val}
    rating = None
    comic = None

    try:
        comic = Comic.objects.get(pk=issue_id)
    except Exception as e:
        rtn_dict["get_comic_error"] = "Unable to find comic"
        rtn_dict["e"] = str(e)

    # check to see if this rating already exists!
    try:
        if comic:
            rating, created = UserRating.objects.get_or_create(user=request.user, comic=comic)
    except Exception as e:
        rtn_dict["get_error"] = "Unable to create or get the rating in question"
        rtn_dict["e"] = str(e)

    if rating:
        if category == "art":
            rating.art = val
        elif category == "story":
            rating.story = val
        elif category == "overall":
            rating.overall = val
        else:
            rtn_dict["cat_error"] = "Unknown Category"

        try:
            rating.save()
            rtn_dict["success"] = True
        except Exception as e:
            rtn_dict["save_error"] = "Unable to save rating"
            rtn_dict["save_e"] = str(e)

    return HttpResponse(json.dumps(rtn_dict), content_type="application/json")
