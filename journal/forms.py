from django import forms
from journal.models import Resource

class AddResourceForm(forms.ModelForm):
    name = forms.CharField(help_text="Enter the title of resource.")
    link = forms.URLField(help_text="Enter the url of resource.")
    software = forms.CharField(help_text="Enter the software.")
    attachment = forms.FileField(help_text="Upload any relevant attachments.")

    class Meta:
        model = Resource
        fields = ('name','link','software','attachment')
