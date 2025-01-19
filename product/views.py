from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


def products(request):
    return render(request, 'product/index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 20
