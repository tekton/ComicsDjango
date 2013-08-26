from django.conf.urls import *
from django.contrib.auth.views import logout
from views import *

urlpatterns = patterns('',
    url(r'add/(\d+)', 'PullLists.views.addToPullList'),
    url(r'covers', 'PullLists.views.recentPullListCovers')
)
