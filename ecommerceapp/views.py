from django.shortcuts import render

from product.models import Product

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:4]
    return render(request, "frontpage.html", {'products': products})

def shop(request):
    products = Product.objects.all()

    return render(request, "shop.html", {'products': products})
