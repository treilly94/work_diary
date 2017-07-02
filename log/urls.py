from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.tom.as_view(), name='tom'),
	url(r'^$', views.base, name='base'),
]
