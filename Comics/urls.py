from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
               url(r'^accounts/', include('auth2.urls', namespace="accounts")),
               url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^comics/', include('HomeComics.urls', namespace="comics")),
               url(r'^issues/', include('issues.urls', namespace="issues")),
               url(r'^files/', include('comicFiles.urls', namespace="files")),
               url(r'^auth/', include('auth2.urls', namespace="auth")),
               url(r'^pull/', include('PullLists.urls', namespace="pulls")),
               url(r'$^', include('HomeComics.urls')),  # doesn't match anything
               ]
