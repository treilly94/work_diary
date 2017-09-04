from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [

    #URL for the homepage
    url(r'^$', views.HomeView, name='index'),
    # Url for registering
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # Url for logging in
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # Url for logging out
    url(r'^logout/$', views.logout_user, name='logout'),

]
