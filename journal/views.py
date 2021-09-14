from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Resource
from django.template import loader
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from journal.models import Resource
from journal.models import Software
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from journal import views
# Create your views here.

def tetris(request):
    output = "hlelp me"
    resources = Resource.objects.all()
    template = loader.get_template('tetris.html')
    context = {
        'resources': resources,
    }
    return render(request, 'home.html', {})

def home_view(request):
    resources = Resource.objects.all()
    softwares = Software.objects.all()
    template =loader.get_template('home.html')
    context = {
        'resources': resources,
        'softwares': softwares
    }
    return HttpResponse(template.render(context, request))

class ResourceCreateView(CreateView):
    model = Resource
    fields = ['name', 'link', 'software', 'attachment']
    template_name = 'resourceForm.html'
    success_url = reverse_lazy('journal:home')

class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['name', 'link', 'software', 'attachment']
    context_object_name = 'resources'
    template_name = 'updateForm.html'
    success_url = reverse_lazy('journal:home')

class ResourceDeleteView(DeleteView):
    model = Resource
    fields = ['name', 'link', 'software', 'attachment']
    context_object_name = 'resources'
    template_name = 'deleteForm.html'
    success_url = reverse_lazy('journal:home')
