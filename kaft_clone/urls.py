
from django.contrib import admin
from django.urls import include, path
from page.views import index
from django.conf import settings
from django.conf.urls.static import static
from product.views import category_show

urlpatterns = [
    path('', index, name='index'),
    path('manage/', include('page.urls'), ),
    path('product/', include('product.urls'), ),
    path('category_show/', category_show, name='category_show'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)