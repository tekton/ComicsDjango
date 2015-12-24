from django.conf.urls import url
from comicFiles import views
from HomeComics import views as hcViews
# Uncomment the next two lines to enable the admin:

urlpatterns = [
    url(r'^primary/(\d+)/(\d+)/(\d+)$', views.makePrimary, name="primary"),
    url(r'^primary/transfer/(\d+)$', views.transferPrimaries, name="tp"),
    url(r'^primary/transfer/(\d+)/(.*)$', views.transferPrimaries, name="tup"),
    url(r'^', hcViews.index, name="index"),
    url(r'^(.*)$', views.view_by_comic_name, name="by_name"),
]
