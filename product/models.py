# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import time
import datetime

from django.db import models
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save

from vendor.items.fields import ThumbnailImageField, MyFileSystemStorage

class Country(models.Model):
    """Country model class"""

    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = [ 'name' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country name'}),
        }

class Brand(models.Model):
    """Brand model class"""

    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = [ 'name' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand name'}),
        }

class Category(models.Model):
    """Category model class"""

    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [ 'name' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category name'}),
        }

class Subcategory(models.Model):
    """Subcategory model class"""

    name = models.CharField(max_length=60)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)

class SubcategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'category',)

class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = [ 'name' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subcategory name'}),
        }

class TypeOrUser(models.Model):
    """TypeOrUser model class"""

    type_or_user = models.CharField(max_length=60)

    def __str__(self):
        return self.type_or_user

    def __unicode__(self):
        return u"%s" % self.type_or_user

class Packing(models.Model):
    text = models.CharField(max_length=23, verbose_name="Packing text")

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name of the Product")
    category = models.ForeignKey( Category, blank = True, null = True )
    subcategory = models.ForeignKey( Subcategory, blank = True, null = True )
    description = models.TextField(null=True, blank=True, verbose_name="Description (optional)")
    packing = models.ForeignKey( Packing, blank = True, null = True )
    size_weight = models.CharField(max_length=60, verbose_name="Size/weight")
    SKU = models.CharField(max_length=60)
    brand = models.ForeignKey( Brand, blank = True, null = True )
    country = models.ForeignKey( Country, blank = True, null = True )
    manifacturere = models.CharField(max_length=60)
    photo = ThumbnailImageField(thumb_width=200, blank = True, null = True, storage=MyFileSystemStorage(), upload_to='products_photo/')
    zero_gst = models.BooleanField( default=True, verbose_name="ZERO GST")
    type_or_user = models.ForeignKey( TypeOrUser, blank = True, null = True )
    retail_unit_price = models.FloatField( default=0.0 )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'brand')


class ProductForm( ModelForm ):
    class Meta:
        model = Product
        exclude = [ "type_or_user", ]
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        self.fields['category'].empty_label = "Select category"
        self.fields['subcategory'].empty_label = "Select subcategory"
        self.fields['packing'].empty_label = "Select packing"
        self.fields['brand'].empty_label = "Select brand"
        self.fields['country'].empty_label = "Select country"

class ProductForm2( ModelForm ):
    class Meta:
        model = Product
        fields = ["zero_gst", "type_or_user", "retail_unit_price", ]
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        self.fields['category'].empty_label = "Select category"
        self.fields['subcategory'].empty_label = "Select subcategory"
        self.fields['packing'].empty_label = "Select packing"
        self.fields['brand'].empty_label = "Select brand"
        self.fields['country'].empty_label = "Select country"

try:
    admin.site.register(Subcategory, SubcategoryAdmin)
    admin.site.register(Category, CategoryAdmin)
    admin.site.register(Product, ProductAdmin)
except:
    pass