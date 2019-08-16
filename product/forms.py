from django import forms
from .models import Category, Product


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = [
            'title',
            'gender',
        ]

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'price',
            'status',
            'product_image',
        ]
