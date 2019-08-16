from django.urls import path
from .views import (
    manage_list,

    #Carousel
    carousel_create,
    carousel_list,
    carousel_update,

    #Page
    page_create,
    page_list,
)


urlpatterns = [
    path('', manage_list, name='manage_list'),
    path('carousel_create/', carousel_create, name='carousel_create'),
    path('carousel_list', carousel_list, name='carousel_list'),
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'),

    #page view
    path('page_create/', page_create, name='page_create'),
    path('page_list/', page_list, name='page_list'),

]