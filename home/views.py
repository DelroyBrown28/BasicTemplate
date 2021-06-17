from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import HomePageCustomisation, HeaderCustomisation


def index(request):
    """Returns the home page."""
    home_page_customisation = HomePageCustomisation.objects.all()
    context = {
        'home_page_customisation' : home_page_customisation,
    }
    return render(request, 'home/index.html', context)


def header_customisation(request):
    
    header_customisation = HeaderCustomisation.objects.all()
    context = {
        'header_customisation' : header_customisation,
    }
    return render(request, 'includes/header.html', context)