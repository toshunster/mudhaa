
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'add/$', views.add_vendor, name="add_vendor" ),
]
