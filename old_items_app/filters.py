import django_filters
from django import forms
from django_filters import CharFilter

from old_items_app.models import Product


class NameFilter(django_filters.FilterSet):
    name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'search name', 'class': 'form-control'}))
    description = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'search description', 'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'description',)


class AdminNameFilter(django_filters.FilterSet):
    seller_details__user__username = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'searchlocation', 'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('seller_details__user__username',)
