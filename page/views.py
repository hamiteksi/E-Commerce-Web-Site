from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Carousel, Page
from .forms import CarouselModelForm, PageModelForm


# User:
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published",
    ).exclude(cover_image='')
    # context['images'] = images
    return render(request, 'home/index.html', context)


def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)

def page_list(request):
    context = dict()
    context['page'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)

def page_create(request):
    context = dict()
    context['title'] = 'Page Create Form'
    context['form'] = PageModelForm()
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
    return render(request, 'manage/form.html', context)


# Admin:
def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)


# stuff not checked
def carousel_update(request, pk):
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    # Show :
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # return redirect('carousel_list')
            messages.success(request, 'guncellendi ;)')
            return redirect('carousel_update', pk)
    return render(request, 'manage/carousel_form.html', context)


# stuff not checked
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_form.html', context)