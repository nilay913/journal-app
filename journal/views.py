from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Resource
from django.template import loader

# Create your views here.

def table(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('table.html')
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))

def tetris(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('tetris.html')
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))

def header(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('header.html')
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))
