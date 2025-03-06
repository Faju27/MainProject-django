from django.contrib.auth.forms import UserCreationForm
from django import forms

from old_items_app.models import LoginView, Seller, Customer, Product, Chat, Comment


class LoginRegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = LoginView
        fields = ("username", "password1", "password2")


class CustomerDetailsForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name')
    email = forms.CharField(label='Enter Email')
    address = forms.CharField(label='Enter Address')
    phone_number = forms.CharField(label='Enter Phone No')

    class Meta:
        model = Customer
        fields = ("name", "email", "address", "phone_number")


class SellerDetailsForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name')
    email = forms.CharField(label='Enter Email')
    address = forms.CharField(label='Enter Address')
    phone_number = forms.CharField(label='Enter Phone No')

    class Meta:
        model = Seller
        fields = ("name", "email", "address", "phone_number", "document")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ("name", "price", "photo", "description")
        fields = "__all__"
        exclude = ('seller_details', )


class ChatForm(forms.ModelForm):
    customer_message = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Type Messages Here', 'class': 'form-control'}), required=False)
    seller_message = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Type Messages Here', 'class': 'form-control'}), required=False)

    class Meta:
        model = Chat
        fields = ("customer_message", "seller_message")


class CommentForm(forms.ModelForm):
    customer_comment = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comment Here', 'class': 'form-control', 'style': 'height:35px;'}), required=False)
    seller_comment = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comment Here', 'class': 'form-control'}), required=False)

    class Meta:
        model = Comment
        fields = ("customer_comment", "seller_comment")
