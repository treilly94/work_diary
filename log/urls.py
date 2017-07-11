from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^users/$', views.UserView.as_view(), name='users'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^createblog/$', views.CreateBlogView.as_view(), name='createblog'),
	url(r'^manageblogs/$', views.ManageBlogView.as_view(), name='manageblogs'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^$', views.base, name='base'),
]
