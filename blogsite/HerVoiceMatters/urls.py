from django.conf.urls import url
from .views import *

app_name = "Blog"
urlpatterns =[
       url(r'^$', HomeView.as_view(), name = "home"),
       url(r'^home$', HomeView.as_view(), name = "home"),
       url(r'^posts/(?P<category>\w*(delicacies|women|fashion|all))/$', PostList.as_view(), name = "posts"),
       url(r'^events$', EventList.as_view(), name = "events"),
       url(r'^gallery$', GalleryList.as_view(), name = "gallery"),
       url(r'^posts/(?P<pk>\d+)/preview/$', PostDetail.as_view(), name = "post_detail"),
       url(r'^events/(?P<pk>\d+)/preview/$', EventDetail.as_view(), name = "event_detail"),
       url(r'^contact/$', ContactView.as_view(), name = "contact"),
       url(r'^about/$', AboutView.as_view(), name = "about"),
]