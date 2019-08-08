from django.urls import path
from .views import (
    carousel_create,
    carousel_list,
    carosuel_update,
)


urlpatterns = [
    path('carousel_create/', carousel_create, name='carousel_create'),
    path('carousel_list', carousel_list, name='carousel_list'),
    path('carousel/update/<slug:pk>/', carosuel_update, name='carousel_update')

]