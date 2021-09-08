from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Resource
from django.template import loader
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from journal.forms import AddResourceForm

# Create your views here.

def tetris(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('tetris.html')
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('home.html')
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))

def add_resource(request):
    form = AddResourceForm(request.POST)

    # Check if the form is valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('all-borrowed'))

def add(request):
    if request.method == "POST" or None:
        form = AddResourceForm(request.POST or None)
        if  form.is_valid():
            form.save()
            return render(request,'journal/table.html',{'form':form})
        else:
            form = AddResourceForm()
            return render(request, 'app/add.html',{'form':form})
    else:
        form = AddResourceForm()
        return render(request, 'journal/add.html')
