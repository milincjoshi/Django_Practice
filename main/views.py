# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
def home(request):
    return HttpResponse("Hello World")
'''
from django.template import loader
def home(request):
    #rendering the template in HttpResponse
    template = loader.get_template('main/home.html')
    return HttpResponse(template.render({'data':"and how you doin"}, request))# this works
    #return HttpResponse(request,"main/home.html") this does not work
