from django.conf.urls import url
from .views import PostList, EventList, GalleryList ,PostDetail ,EventDetail,HomeView

app_name = "Blog"
urlpatterns =[
       url(r'^home$', HomeView.as_view(), name = "home"),
       url(r'^$', HomeView.as_view(), name = "home"),
       url(r'^posts$', PostList.as_view(), name = "posts"),
       url(r'^events$', EventList.as_view(), name = "events"),
       url(r'^gallery$', GalleryList.as_view(), name = "gallery"),
       url(r'^posts/(?P<pk>\d+)/preview/$', PostDetail.as_view(), name = "post_detail"),
       url(r'^events/(?P<pk>\d+)/preview/$', EventDetail.as_view(), name = "event_detail"),
]