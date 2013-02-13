from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',  # /series
    url(r'^$', 'issues.views.index'),
    #url(r'/issue/(.*)/(.*)/(.*)$','HomeComics.views.issue_search_issue'), ### Series / volume / number
    url(r'^/(\d+)$', 'issues.views.browse'),
    url(r'^/increment/(\d+)', 'issues.views.incrementSeries'),
    #url(r'/search','HomeComics.views.search'),
    #url(r'/recent','HomeComics.views.recent_by_id'),
    url(r'/issue/(.*)', 'issues.views.single'),
    #url(r'/new_series','HomeComics.views.recent_by_id'),
    #url(r'/view/dirpath$','HomeComics.views.view_dir_path'),
    #url(r'/view/paths','HomeComics.views.view_dir_paths_list'),
    url(r'/ajax/series/all', 'stories.views.getSeriesList'),
    url(r'/ajax/series/(\d+)', 'stories.views.getComicsFromSeries'),
    url(r'/ajax/series/add/(\d+)/(\d+)', 'stories.views.addIssueToStory'),  # series // comic id
    url(r'/arc/new', 'stories.views.newArcDisplay'),
    url(r'/ajax/(\d+)/(.*)', 'issues.views.toggle_box'),
)
