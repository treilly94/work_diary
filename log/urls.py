from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    # blog homepage  ----   /blogs/
    url(r'^$', views.index_blog, name='index_blog'),

    # viewing a single blog --- /blog/<blog id>/
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail_blog, name="detail_blog"),
 ]
