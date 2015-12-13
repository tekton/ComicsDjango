from django.conf.urls import *
from PullLists import views

urlpatterns = [
    url(r'add/(\d+)', views.addToPullList),
    url(r'covers', views.recentPullListCovers),
    url(r'delete/(\d+)', views.deleteList),
    url(r'owned', views.ownedSeriesList),
    url(r'missing', views.missing),
    url(r'^', views.currentList),
]
