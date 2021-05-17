from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product



def all_products(request):
    """Shows and displays all products."""
    products = Product.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search query!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    
    product_context = {
        'products' : products,
        'search_term' : query,
    }
    
    return render(request, 'products/products.html', product_context)



def product_detail(request, product_id):
    """Displays individual products."""
    product = get_object_or_404(Product, pk=product_id)
    
    product_context = {
        'product' : product,
    }
    
    return render(request, 'products/product_detail.html', product_context)

