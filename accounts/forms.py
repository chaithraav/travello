from django import forms
from .models import review

class reviewForm(forms.ModelForm):

    class Meta:
        model = review
        fields =['name','email','opinion','rate']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.TextInput(attrs = {'class' : 'form-control'}),
            'opinion': forms.TextInput(attrs = {'class' : 'form-control'}),
            'rate': forms.Select(attrs = {'class' : 'form-control'}),
        }