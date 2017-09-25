# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from product.models import ProductForm, Category
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

@csrf_exempt
def get_subcategory( request ):
    esponse_dic = dict()
    # html page of the form
    form_template='subcategory_template.html'
    response_dic = dict()
    print( "ahaha", request )
    if request.method == 'POST':
        print( request.POST )
        if 'category' in request.POST:
            category_id = request.POST['category']
            subcateogies = list()
            try:
                category = Category.objects.get(id=int(category_id))
            except Exception as e:
                print("ERROR: {0}".format(str(e)))
                return ""
            response_dic['subcategories'] = category.subcategory_set.all()

            return HttpResponse(render_to_string(form_template, response_dic, RequestContext(request)))
    return ""