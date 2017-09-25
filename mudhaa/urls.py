from django.conf.urls import patterns, include, url

from django.contrib import admin

from mudhaa.views import main_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vendor/', include('vendor.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^$', main_view ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
