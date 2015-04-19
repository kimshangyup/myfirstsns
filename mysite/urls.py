from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/','blog.views.test'),
 	url(r'^write/','blog.views.write'),
 	url(r'^blog/(\d+)/','blog.views.blog'),
 	url(r'^blog/comment/(\d+)/','blog.views.blog_comment'),
 	url(r'^blog/comment/delete/(\d+)/','blog.views.blog_comment_delete'),	
)
