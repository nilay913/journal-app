from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Resource

# Create your views here.

def index(request):
    output = "hlelp me"
#    resources = Resource.object.all()
#    resource_list = ", ".join([r.name for r in resources])
    return HttpResponse(output)
