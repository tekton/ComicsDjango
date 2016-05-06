from django.conf.urls import url
from HomeComics import views
from HomeComics import search

urlpatterns = [
    url(r'issue/(.*)/(.*)/(.*)$', views.issue_search_issue, name="issue_search"),  # Series / volume / number
    url(r'^(\d+)$', views.single_issue, name="single"),
    url(r'search', search.search_all, name="search"),
    url(r'recent', views.recent_by_id, name="recent"),
    url(r'new_series/(.*)',  views.new_series_from_data, name="new_series"),
    url(r'view/dirpath$',  views.view_dir_path, name="dirpath"),
    url(r'view/paths',  views.view_dir_paths_list, name="paths"),
    url(r'possible',  views.possible_series_list, name="possible"),
    url(r'ajax/transfer/(\d+)',  views.to_transfer_single_issue, name="transfer"),
    url(r'series/all', views.known_series_list, name="series_all"),
    url(r'api/1.0/thumbnails/(\d+)$', views.api_thumbnail_strip, name="thumbs"),
    url(r'api/1.0/thumbnails', views.api_thumbnail_strip, name="thumbs"),
    url(r'^angular', views.angular_test, name="angular"),
    url(r'^', views.index, name="index"),
]
