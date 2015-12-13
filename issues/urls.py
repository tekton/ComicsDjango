from django.conf.urls import url
from issues import views
from stories import views as storyViews
from HomeComics import views as hcViews
from ratings import views as ratingViews
# Uncomment the next two lines to enable the admin:

urlpatterns = [  # /series
    url(r'^', views.index),
    url(r'^(\d+)$', views.browse),
    url(r'^increment/(\d+)', views.incrementSeries),
    url(r'issue/(.*)', views.single),
    url(r'ajax/series/all', storyViews.getSeriesList),
    url(r'ajax/series/(\d+)', storyViews.getComicsFromSeries),
    url(r'ajax/series/add/(\d+)/(\d+)', storyViews.addIssueToStory),  # series // comic id
    url(r'arc/new', storyViews.newArcDisplay),
    url(r'ajax/set/(\d+)/(art|story|overall)/(.*)', ratingViews.set_user_rating),
    url(r'ajax/transfer/(\d+)', hcViews.to_transfer_single_issue),
    url(r'ajax/(\d+)/(.*)', views.toggle_box),
]
