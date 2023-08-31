from django import forms
from .models import Students


class Std_form(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'  
        # exclude = ['password']

class LogCredent(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)

