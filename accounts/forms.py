# posts/forms.py
from django import forms
from .models import upload, results


class uploadForm(forms.ModelForm):

    class Meta:
        model = upload
        fields = ['uploadText', 'upload']


class resultsForm(forms.ModelForm):

    class Meta:
        model = results
        fields = ['genome_size', 'repeat', 'tax_ID', 'dist']
        #fields = ['Closest genome size', 'Repeat content', 'Taxonomically identification', 'Distance from the taxonomically closest genome']