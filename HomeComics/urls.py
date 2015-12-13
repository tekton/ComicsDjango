from django.conf.urls import url
from HomeComics import views
from HomeComics import search

urlpatterns = [
    url(r'^', views.index),
    url(r'issue/(.*)/(.*)/(.*)$', views.issue_search_issue),  # Series / volume / number
    url(r'^(\d+)$', views.single_issue),
    url(r'search', search.search_all),
    url(r'recent', views.recent_by_id),
    url(r'new_series/(.*)',  views.new_series_from_data),
    url(r'view/dirpath$',  views.view_dir_path),
    url(r'view/paths',  views.view_dir_paths_list),
    url(r'possible',  views.possible_series_list),
    url(r'ajax/transfer/(\d+)',  views.to_transfer_single_issue),
    url(r'series/all', views.known_series_list),
]
