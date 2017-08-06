from django.conf.urls import url
from . import views


urlpatterns = [
    # blog homepage  ----   /blogs/
    url(r'^$', views.index_blogs, name='index_blogs'),
    # create blogs  ----  /blogs/create_blogs/
    url(r'^create_blog$', views.create_blogs, name='create_blogs'),
    # manage your blog  ----   /blogs/manage/
    url(r'^manage/$', views.manage_blogs, name='manage_blogs'),
    # View blog  ----   /blogs/<blog id>/
    url(r'^(?P<blog_id>[0-9]+)/$', views.view_blogs, name='view_blogs'),
    # Favourite a blog ---  /blogs/<blog title>//favourite
    # url(r'^(?P<log_id>[0-9]+)/favourite$', views.view_blogs, name='fave_blogs'),
 ]
