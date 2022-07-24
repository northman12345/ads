from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm): 
    email = forms.EmailField(required= True, widget= forms.EmailInput(attrs={'class':'form-control', 'placeholder':'demo@gmail.com'}))
    username =forms.CharField(required= True, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1 =forms.CharField(required= True, widget= forms.PasswordInput(attrs={'class':'form-control pr-password', 'placeholder':'*******','id':'mypassword',}))
    password2 =forms.CharField(required= True, widget= forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'*******','id':'confirm_mypassword'}))


    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        #get the email
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact = email).exists():
            raise forms.ValidationError("user with that email alread exist")
        return email

        