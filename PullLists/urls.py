from django.conf.urls import *
# from views import *

urlpatterns = patterns('',
    url(r'/add/(\d+)', 'PullLists.views.addToPullList'),
    url(r'/covers', 'PullLists.views.recentPullListCovers'),
    url(r'/delete/(\d+)', 'PullLists.views.deleteList'),
    url(r'/owned', 'PullLists.views.ownedSeriesList'),
    url(r'/missing', 'PullLists.views.missing'),
    url(r'^$', 'PullLists.views.currentList'),
    url(r'/^$', 'PullLists.views.currentList'),
)
