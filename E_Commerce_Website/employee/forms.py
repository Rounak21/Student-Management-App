from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ['first_name', 'last_name', 'email','username', 
        ]

    def clean_email(self):
        if not self.cleaned_data['email'].endswith('gmail.com'):
            raise ValidationError("Please check your email, it should end with gmail.com")
    
    def save(self,commit=True):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u



class ProfileForm(forms.ModelForm):

    class Meta:
        model= Profile
        fields= ('salary', 'designation')


    def clean_salary(self):
        if self.cleaned_data.get('salary') > 500000:
            raise ValidationError('Salary is very high')



