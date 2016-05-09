from django.conf.urls import url
from issues import views
from stories import views as storyViews
from HomeComics import views as hcViews
from ratings import views as ratingViews
# Uncomment the next two lines to enable the admin:

urlpatterns = [  # /series
    url(r'issue/(.*)', views.single, name="single"),
    url(r'^api/1.0/series_issues/(\d+)', views.api_series_issues, name="api_series_issues"),
    url(r'^(\d+)$', views.browse, name="browse"),
    url(r'increment/(\d+)', views.incrementSeries, name="increment"),
    url(r'ajax/series/all', storyViews.getSeriesList, name="series_all"),
    url(r'ajax/series/(\d+)', storyViews.getComicsFromSeries, name="series_single"),
    url(r'ajax/series/add/(\d+)/(\d+)', storyViews.addIssueToStory, name="ajax_add_to_story"),  # series // comic id
    url(r'arc/new', storyViews.newArcDisplay, name="arc_new"),
    url(r'ajax/set/(\d+)/(art|story|overall)/(.*)', ratingViews.set_user_rating, name="ajax_rating"),
    url(r'ajax/transfer/(\d+)', hcViews.to_transfer_single_issue, name="ajax_transfer"),
    url(r'ajax/(\d+)/(.*)', views.toggle_box, name="ajax_toggle"),
    url(r'$^', views.index, name="index"),
]
