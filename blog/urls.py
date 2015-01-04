from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'author/(?P<author_name>[a-zA-Z0-9-_]+)$', views.author, name='author'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<post_slug>.*)/comment/$', views.add_comment, name='add_comment'),
    url(r'(?P<post_slug>.*)', views.detail, name='detail'),
)
