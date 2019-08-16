from django import forms
from .models import Carousel, Page


class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        # fields = '__all__'
        fields = [
            'title',
            'cover_image',
        ]

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title',
            'content',
            'status',
            'coverimage'
        ]
