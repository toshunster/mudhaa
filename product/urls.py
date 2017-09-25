
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'add/$', views.add_product, name="add_product" ),
    url(r'^subcategories/$', views.get_subcategory, name='get_subcategory'),
]
