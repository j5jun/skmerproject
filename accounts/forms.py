# posts/forms.py
from django import forms
from .models import upload


class uploadForm(forms.ModelForm):

    class Meta:
        model = upload
        fields = ['uploadText', 'upload']


