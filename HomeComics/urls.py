from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
	url(r'^$','HomeComics.views.index'),
	url(r'/issue/(.*)/(.*)/(.*)$','HomeComics.views.issue_search_issue'), ### Series / volume / number
	url(r'^/(\d+)$','HomeComics.views.single_issue'),
	url(r'/search','HomeComics.views.search'),
	url(r'/recent','HomeComics.views.recent_by_id'),
	url(r'/new_series/(.*)','HomeComics.views.new_series_from_data'),
	#url(r'/new_series','HomeComics.views.recent_by_id'),
)
