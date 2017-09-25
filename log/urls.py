from django.conf.urls import url
from django.contrib.auth import authenticate, login
from . import views

app_name = "blog"
urlpatterns = [

    # blog homepage  ----   /blogs/
    url(r'^$', views.IndexBlogView.as_view(), name='index_blog'),

    # viewing a single blog --- /blog/<blog id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailBlogView.as_view(), name="detail_blog"),

    # Url for creating a blog
    url(r'add-blog/$', views.BlogCreate.as_view(), name='blog-add'),

    # edit a single blog --- /blog/<blog id>-edit/
    url(r'^(?P<pk>[0-9]+)-edit/$', views.UpdateBlog.as_view(), name="edit_blog"),
    # delete a single blog --- /blog/<blog id>-delete/
    url(r'^(?P<pk>[0-9]+)-delete/$', views.DeleteBlog.as_view(), name="delete_blog"),
 ]
