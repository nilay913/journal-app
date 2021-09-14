from django import forms
from journal.models import Resource
from journal.models import Software

class AddResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'link', 'software', 'attachment',]

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            return super().form_valid(form)

class AddSoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            return super().form_valid(form)
