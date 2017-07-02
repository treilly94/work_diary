from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^users/$', views.UserView.as_view(), name='users'),
    url(r'^fields/$', views.FieldView.as_view(), name='fields'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^$', views.base, name='base'),
]
