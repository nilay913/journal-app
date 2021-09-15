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
    return render(request, 'tetris.html', {})

def pacman(request):
    return render(request, 'pacman.html', {})

def spaceInvaders(request):
    return render(request, 'spaceInvaders.html', {})

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

    def resourceForm(request):
        if request.method == 'POST':
            form = AddResourceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('journal:home')
        else:
            form = AddResourceForm()
        return render(request, 'core/resourceForm.html', {
            'form': form
        })

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

class SoftwareCreateView(CreateView):
    model = Software
    fields = ['SoftwareTag']
    template_name = 'addSoftware.html'
    success_url = reverse_lazy('journal:home')

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())
