# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from vendor.models import VendorForm

def add_vendor( request ):
    form = VendorForm()
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = VendorForm()
    return render_to_response( 'new_vendor.html', context_instance = RequestContext( request, { 'form': form } ) )
