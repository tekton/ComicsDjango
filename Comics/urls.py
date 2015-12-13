from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
               # Examples:
               # url(r'^$', 'Comics.views.home', name='home'),
               # url(r'^Comics/', include('Comics.foo.urls')),
               # Uncomment the admin/doc line below to enable admin documentation:
               url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

               # Uncomment the next line to enable the admin:
               url(r'^admin/', include(admin.site.urls)),

               url(r'^', include('HomeComics.urls')),
               url(r'^comics', include('HomeComics.urls')),
               #
               url(r'^issues', include('issues.urls')),
               #
               url(r'^files', include('comicFiles.urls')),
               #
               url(r'^auth', include('auth2.urls')),
               #
               url(r'^pull', include('PullLists.urls')),
               #
               url(r'^accounts', include('auth2.urls')),
               ]
