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

    # Url for creating an account
    url(r'^create_account/$', views.CreateAccountView.as_view(), name='create_account'),
    # Url for creating an account
    url(r'^account/$', views.AccountView, name='view_account'),
    # Url for Editing an account
    url(r'^account-edit/$', views.UpdateAccountView, name='edit_account'),
    # Url for Deleting an account
    url(r'^deactivate-account/$', views.DeactivateAccount, name='deactivate_account'),
]

# (?P<pk>[0-9]+)