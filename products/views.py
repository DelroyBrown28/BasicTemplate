from django.shortcuts import render
from .models import Product

def all_products(request):
    """Shows and displays all products."""
    
    products = Product.objects.all()
    
    product_context = {
        'products' : products,
    }
    
    return render(request, 'products/products.html', product_context)
