from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/blog/'}),
)
