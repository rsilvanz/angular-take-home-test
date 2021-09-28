from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.swagger.views import schema_view
from apps.location.urls import urlpatterns as location_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^location/', include(location_urls)),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
