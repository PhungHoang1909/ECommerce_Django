from django.shortcuts import render

from product.models import Product, Category

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:4]
    return render(request, "frontpage.html", {'products': products})

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/shop.html', context)
