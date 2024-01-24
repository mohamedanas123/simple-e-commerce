from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# for creating login form

class loginform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Your Name ',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))



# for creating signup form

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Your Name ',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter Your Email',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password Again',
        'class':'w-full py-4 px-6 rounded-xl',
    }))