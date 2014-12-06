from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # TODO: change post_id to use slug of post, mind the model too
    url(r'(?P<post_id>\d)', views.detail, name='detail'),
    url(r'author/(?P<author_name>[a-zA-Z0-9-_]+)', views.author, name='author'),
)
