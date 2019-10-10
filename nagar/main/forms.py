from django import forms
from .models import service


class serviceForm(forms.Form):
    name = forms.CharField(label='Enter Title', help_text='Custom CMS',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'cols': "80", 'rows': "10", 'class': 'form-control'}))