from django.conf.urls import *
from PullLists import views

api_1_0 = [
    url(r"^list", views.api_current_list, name="list"),
    url(r"^remove/(\d+)", views.api_remove_pull, name="remove")
]

apis = [
    url(r"^1.0/", include(api_1_0, namespace="1.0"))
]

urlpatterns = [
    url(r'add/(\d+)', views.addToPullList, name="add"),
    url(r'covers', views.recentPullListCovers, name="covers"),
    url(r'delete/(\d+)', views.deleteList, name="delete"),
    url(r'owned', views.ownedSeriesList, name="owned"),
    url(r'missing', views.missing, name="missing"),
    # url(r"api/1.0/list", views.api_current_list, name="api_current"),
    url(r"api/", include(apis, namespace="api")),
    url(r'^', views.currentList, name="index"),
]
