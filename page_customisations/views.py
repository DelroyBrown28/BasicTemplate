from django.shortcuts import render
from .models import (HomePageCustomisation,
                     HeaderCustomisation,
                     ProductsPageCustomisation)


def header_customisation(request):
    """Customisation for header contents"""
    header_customisation = HeaderCustomisation.objects.all()
    context = {
        'header_customisation' : header_customisation,
    }
    return render(request, 'includes/header.html', context)


def products_page_customisation(request):
    """Customisation for products page"""
    products_page_customisation = ProductsPageCustomisation.objects.all()
    context = {
        'products_page_customisation' : products_page_customisation,
    }
    return render(request, 'products/products.html', context)


