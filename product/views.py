# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from product.models import ProductForm
from vendor.models import PriceProductForm

def add_product( request ):
    product_form = ProductForm()
    price_product_form = PriceProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        price_product_form = PriceProductForm(request.POST, request.FILES)
        if product_form.is_valid() and price_product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            price_product = price_product_form.save(commit=False)
            price_product.product = product
            price_product.save()
            
        
    return render_to_response( 'new_product.html', context_instance = RequestContext( request, { 'product_form': product_form, 'price_product_form' : price_product_form } ) )
