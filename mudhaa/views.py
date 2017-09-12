from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from vendor.models import Vendor
import datetime

# Main page view
def main_view( request ):
    vendors = Vendor.objects.all()
    return render_to_response( 'base.html', context_instance = RequestContext( request, { 'vendors' : vendors } ) )

