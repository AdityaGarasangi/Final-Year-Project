from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password2",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserBasicInfoForm(ModelForm):
    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "username",
        }


class UserMoreInfoForm(forms.ModelForm):
    upload = forms.ImageField(label="Profile Picture")

    class Meta:
        model = Profile
        fields = {"email", "occupation", "location", "birth_date", "upload"}
        exclude = {
            "user",
        }
