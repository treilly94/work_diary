from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.tom, name='tom'),
	url(r'^$', views.base, name='base'),
]
