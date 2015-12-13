from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
               url(r'^accounts', include('auth2.urls')),
               url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^comics', include('HomeComics.urls')),
               url(r'^issues', include('issues.urls')),
               url(r'^files', include('comicFiles.urls')),
               url(r'^auth', include('auth2.urls')),
               url(r'^pull', include('PullLists.urls')),
               url(r'$^', include('HomeComics.urls')),  # doesn't match anything
               ]
