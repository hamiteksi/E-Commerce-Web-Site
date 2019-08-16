from django.urls import path
from .views import (
    #CATEGORY
    category_create,

    #PRODUCT
    product_create,
    product_view,

)


urlpatterns = [
    path('products/', product_view, name='product_view'),
    path('products_create', product_create, name='products_create'),
    #category view
    path('category_create/', category_create, name='category_create'),
]