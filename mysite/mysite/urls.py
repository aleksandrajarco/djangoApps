from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#url(r'^admin/', include(admin.site.urls)),
#    url(r'', include('blog.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#url(r'^$', views.post_list),
#    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
)
