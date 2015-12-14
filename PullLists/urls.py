from django.conf.urls import *
from PullLists import views

urlpatterns = [
    url(r'add/(\d+)', views.addToPullList, name="add"),
    url(r'covers', views.recentPullListCovers, name="covers"),
    url(r'delete/(\d+)', views.deleteList, name="delete"),
    url(r'owned', views.ownedSeriesList, name="owned"),
    url(r'missing', views.missing, name="missing"),
    url(r'^', views.currentList, name="index"),
]
