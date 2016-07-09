from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('decode.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', admin.site.urls),
]
