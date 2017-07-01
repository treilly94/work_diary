from django.conf.urls import url
#from log import views as core_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.base, name='home'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'account/login'}, name='logout'),
	url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate')
    ]
	
#url(r'^$', views.index, name='index'),
#url(r'^$', views.tom, name='tom'),
#url(r'^$', views.base, name='base')