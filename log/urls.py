from django.conf.urls import url
from django.contrib.auth import authenticate, login
from . import views

app_name = "blog"
urlpatterns = [

    # blog homepage  ----   /blogs/
    url(r'^$', views.IndexBlogBiew.as_view(), name='index_blog'),

    # viewing a single blog --- /blog/<blog id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailBlogView.as_view(), name="detail_blog"),

    # Url for creating a blog
    url(r'add-blog/$', views.BlogCreate.as_view(), name='blog-add'),

    # Url for editing a blog
    url(r'manage-blog/(?P<pk>[0-9]+)/edit$', views.BlogUpdate.as_view(), name='blog-update'),

    # Url for deleting a blog
    url(r'delete-blog/(?P<pk>[0-9]+)/delete$', views.BlogDelete.as_view(), name='blog-delete'),
 ]
