from django import forms
from django.db.models import fields
from .models import Emp

class EmpRegistration(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }