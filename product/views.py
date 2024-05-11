from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product.html', {'product': product})