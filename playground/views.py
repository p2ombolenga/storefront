from django.shortcuts import render
from store.models import Product

def say_hello(request):
    products = Product.objects.filter(title__icontains='lemon')
    return render(request, 'hello.html', {'name': 'peter', 'products': list(products)})