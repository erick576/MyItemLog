from django import forms
from django.forms import Textarea

from .models import entry


class EntryForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = entry
        fields = [
            'Item',
            'Picture_URL',
            'Description',
            'Price',
            'Date',
            'URL',
            'user',
        ]
        widgets = {
            'Description': Textarea(attrs={'cols': 23, 'rows': 10}),
        }




class RawEntryForm(forms.Form):
    Item = forms.CharField()
    Picture_URL = forms.URLField()
    Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 20,
        }
    ))
    Price = forms.DecimalField()
    Date = forms.DateField()
    URL = forms.URLField()
