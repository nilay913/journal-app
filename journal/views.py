from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Resource
from django.template import loader

# Create your views here.

def index(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('table.html')
    name_list = ", ".join([r.name for r in resources])
    link_list = ", ".join([r.link for r in resources])
    software_list = ", ".join([r.software for r in resources])
    attachment_list = ", ".join(["attachment" for r in resources])
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))
