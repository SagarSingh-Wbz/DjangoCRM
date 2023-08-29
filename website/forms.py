from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email= forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    firstName=forms.CharField(label="",max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    lastName=forms.CharField(label="",max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))


    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')