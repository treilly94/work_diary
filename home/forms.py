from django.contrib.auth.models import User
from django import forms
from .models import Account


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'password',]



class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class UserSettingsExtendedForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('location', 'date_of_birth',)