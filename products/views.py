from django.shortcuts import render, get_object_or_404
from .models import Product




def all_products(request):
    """Shows and displays all products."""
    products = Product.objects.all()
    
    product_context = {
        'products' : products,
    }
    
    return render(request, 'products/products.html', product_context)



def product_detail(request, product_id):
    """Displays individual products"""
    product = get_object_or_404(Product, pk=product_id)
    
    product_context = {
        'product' : product,
    }
    
    return render(request, 'products/product_detail.html', product_context)

