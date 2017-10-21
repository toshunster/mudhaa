from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save
from vendor.items.fields import ThumbnailImageField, MyFileSystemStorage
from product.models import Country, Product

import re
import time
import datetime

class Vendor(models.Model):
    """Country model class"""

    name = models.CharField(max_length=60)
    address = models.CharField(max_length=360, blank=True, null=True )
    tin = models.CharField(max_length=60, blank=True, null=True )
    contact_number = models.CharField(max_length=20, blank=True, null=True )
    fax_number = models.CharField(max_length=20, blank=True, null=True )
    email = models.CharField(max_length=30, blank=True, null=True )
    website = models.CharField(max_length=120, blank=True, null=True )
    fb_page = models.CharField(max_length=120, blank=True, null=True )
    twitter = models.CharField(max_length=120, blank=True, null=True )
    instagram = models.CharField(max_length=120, blank=True, null=True )
    country = models.ForeignKey(Country, blank=True, null=True)
    contact_person = models.CharField(max_length=60, blank=True, null=True )
    logo = ThumbnailImageField(thumb_width=200, blank = True, null = True, storage=MyFileSystemStorage(), upload_to='logos/')
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class VendorForm(ModelForm):
    
    class Meta:
        model = Vendor
        exclude = [ ]#'__all__'
    
    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        self.fields['country'].empty_label = "Select country"

class PriceProduct(models.Model):
    vendor = models.ForeignKey( Vendor )
    product = models.ForeignKey( Product )
    price = models.FloatField( default=0.0 )

class PriceProductForm(ModelForm):
    class Meta:
        model = PriceProduct
        exclude = [ "product", ]
    
    def __init__(self, *args, **kwargs):
        super(PriceProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        self.fields['vendor'].empty_label = "Select vendor"

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

class PriceProductAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'product', 'price')

try:
    admin.site.register(Vendor, VendorAdmin)
    admin.site.register(PriceProduct, PriceProductAdmin)
except:
    pass