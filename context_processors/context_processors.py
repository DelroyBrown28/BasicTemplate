from home.views import HeaderCustomisation
from products.models import ProductsPageCustomisation


def header_customisation_processor(request):
    return {
       'header_customisation': HeaderCustomisation.objects.all(),

    }
    
def products_page_customisation_processor(request):
    return {
       'products_page_customisation': ProductsPageCustomisation.objects.all(),
    }
