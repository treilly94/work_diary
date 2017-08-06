from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('log.urls', namespace='blogs')),
    url(r'^admin/', admin.site.urls),
]
