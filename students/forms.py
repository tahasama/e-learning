from django import forms
from courses.models import Course

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.HiddenInput)


class UserCreationEmailForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name' )