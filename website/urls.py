from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('product.urls')),
    path('servicos/', include('service.urls')),
    path('orcamentos/', include('estimate.urls')),
]
