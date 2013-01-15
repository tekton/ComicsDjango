from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
	url(r'^$','HomeComics.views.index'),
	url(r'/issue/(.*)/(.*)/(.*)$','HomeComics.views.issue_search_issue'), ### Series / volume / number
	url(r'^/(\d+)$','HomeComics.views.single_issue'),
	url(r'/search','HomeComics.search.search_all'),
	url(r'/recent','HomeComics.views.recent_by_id'),
	url(r'/new_series/(.*)','HomeComics.views.new_series_from_data'),
	#url(r'/new_series','HomeComics.views.recent_by_id'),
	url(r'/view/dirpath$','HomeComics.views.view_dir_path'),
	url(r'/view/paths','HomeComics.views.view_dir_paths_list'),
	url(r'/possible',"HomeComics.views.possible_series_list"),
	url(r'/ajax/transfer/(\d+)','HomeComics.views.to_transfer_single_issue'),
)
