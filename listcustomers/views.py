from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import TblDueListing

# the view to display the customer information
def index(request):
    customers = TblDueListing.objects.all()
    template = loader.get_template('listcustomers/index.html')
    context = {
        'customers': customers,
    }
    return HttpResponse(template.render(context, request))
