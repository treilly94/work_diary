from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [

    #URL for the homepage
    url(r'^$', views.HomeView, name='index'),
    # Url for registering
    url(r'^register/$', views.registration, name='register'),
    # Url for logging in
    url(r'^login_user/$', views.login_user, name='login_user'),
    # Url for logging out
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]
