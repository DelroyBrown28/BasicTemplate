from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import HomePageCustomisation


def index(request):
    """Returns the home page."""
    home_page_customisation = HomePageCustomisation.objects.all()
    return render(request, 'home/index.html', {"home_page_customisation" : home_page_customisation})


