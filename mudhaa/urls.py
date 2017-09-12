from django.conf.urls import patterns, include, url

from django.contrib import admin

from views import main_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vendor/', include('vendor.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^$', main_view ),
]
