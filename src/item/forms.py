from django import forms
from django.forms import Textarea

from .models import entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = entry
        fields = [
            'Item',
            'Picture_URL',
            'Description',
            'Price',
            'Date',
            'URL',
        ]
        widgets = {
            'Description': Textarea(attrs={'cols': 23, 'rows': 10}),
        }

