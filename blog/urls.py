from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'author/(?P<author_name>[a-zA-Z0-9-_]+)$', views.author, name='author'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<post_slug>.*)', views.detail, name='detail'),
    url(r'comment/(?P<comment_id>[0-9]+)', views.CommentView.as_view(), name='comment'),
)
