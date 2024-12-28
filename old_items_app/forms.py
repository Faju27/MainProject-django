from django.contrib.auth.forms import UserCreationForm
from django import forms

from old_items_app.models import LoginView, Seller, Customer


class LoginRegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = LoginView
        fields = ("username", "password1", "password2")


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "email", "address", "phone_number")


class SellerDetailsForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ("name", "email", "address", "phone_number", "document")
