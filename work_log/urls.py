from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('log.urls')),
    url(r'^', include('log.urls')),
]
