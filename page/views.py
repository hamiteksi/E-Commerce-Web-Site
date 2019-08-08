from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    return render(request, 'home/index.html', context)

def carousel_list(request):
    context = {}
    context['carousel'] = Carousel.objects.all()
    return render(request, 'manage/carousel_list.html', context)

def carosuel_update(request, pk):
    context = {}
    item = Carousel.objects.get(pk = pk)
    form = CarouselModelForm(instance=item)
    context['item']= item
    context['form'] = form

    return render(request, 'manage/carousel_update.html', context)

def carousel_create(request):
    context = {}
    # item = Carousel.objects.first()
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES['cover_image'])
        form = CarouselModelForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_create.html', context)



#deneme = Carousel.objects.filter(title='#request.post.get('title')#')
#deneme.first().cover_image