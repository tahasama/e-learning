from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course,Module,fields=['title','description'], 
                                                                extra=2,
                                                                can_delete=True                                                              
                                                                )
class SearchForm(forms.Form):
    query = forms.CharField(label=False,widget=forms.TextInput(attrs=dict(placeholder=(" hit enter to search"))))