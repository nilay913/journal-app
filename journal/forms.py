from django import forms
from journal.models import Resource


class AddResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            return super().form_valid(form)

