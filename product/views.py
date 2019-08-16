from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Product, Category
from .forms import CategoryModelForm, ProductModelForm

#CATEGORY
def category_create(request):
    context = dict()
    context['title'] = 'Category Create Form'
    context['form'] = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
    return render(request, 'manage/form.html', context)

def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)
    context['categories'] = Category.objects.all()
    return render(request, 'product/product_view.html', context)


#PRODUCT
def product_view(request):
    context = dict()
    context['products'] = Product.objects.all().order_by('-pk')
    return render(request, 'product/product_view.html', context)


def product_create(request):
    context = dict()
    context['title'] = 'Product Create Form'
    context['form'] = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
    return render(request, 'manage/form.html', context)



