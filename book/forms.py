from django import forms
from .models import reservation,Payment

class reservationForm(forms.ModelForm):

    class Meta:
        model = reservation
        fields = ['name','gender','age','no_of_people','address','email','phone_no']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'gender': forms.Select(attrs = {'class' : 'form-control'}),
            'age': forms.TextInput(attrs = {'class' : 'form-control'}),
            'no_of_people': forms.TextInput(attrs = {'class' : 'form-control'}),
            'address': forms.TextInput(attrs = {'class' : 'form-control'}),
            'email': forms.TextInput(attrs = {'class' : 'form-control'}),
            'phone_no': forms.TextInput(attrs = {'class' : 'form-control'}),
        }

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['card','card_no','cvv','expiry','email']
        widgets = {
            #'pay': forms.Select(attrs = {'class':'form-control'}),
            'email': forms.TextInput(attrs = {'class':'form-control'}),
            'card': forms.Select(attrs = {'class':'form-control'}),
            'card_no': forms.TextInput(attrs = {'class':'form-control'}),
            'CVV': forms.TextInput(attrs = {'class':'form-control'}),
            'expiry': forms.TextInput(attrs = {'class':'form-control'}),
            #'online': forms.Select(attrs = {'class': 'form-control'}),
            #'upi': forms.TextInput(attrs ={'class':'form-control'}),
        }
        