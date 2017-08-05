from django.conf.urls import url
from . import views

urlpatterns = [
    #blog homepage  ----   /blogs/
    url(r'^$', views.index_blogs, name='index_blogs'),

    # create blogs   ----   /blogs/
    url(r'^blogs/create_blog$', views.create_blogs, name='create_blogs'),
    #manage your blog  ----   /blogs/
    url(r'^blogs/manage$', views.manage_blogs, name='manage_blogs'),
    # View blog  ----   /blogs/
    url(r'^(?P<title>[0-9]+)$', views.view_blogs, name='view_blogs'),
]
