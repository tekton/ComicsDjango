from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^/primary/(\d+)/(\d+)/(\d+)$', 'comicFiles.views.makePrimary'),
    url(r'^/primary/transfer/(\d+)$', 'comicFiles.views.transferPrimaries'),
    url(r'^/primary/transfer/(\d+)/(.*)$', 'comicFiles.views.transferPrimaries'),
    url(r'^$', 'HomeComics.views.index'),
    #url(r'/issue/(.*)/(.*)/(.*)$','HomeComics.views.issue_search_issue'), ### Series / volume / number
    url(r'^/(.*)$', 'comicFiles.views.view_by_comic_name'),
    #url(r'/search','HomeComics.views.search'),
)
