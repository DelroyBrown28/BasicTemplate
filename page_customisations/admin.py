from django.contrib import admin
from page_customisations.models import (HomePageCustomisation,
                                        HeaderCustomisation,
                                        ProductsPageCustomisation)
from BasicTemplateMain.admin import superadmin


# Superuser admin models
class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'home_page_styling',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',
       
    )

    
class HeaderCustomisationAdmin(admin.ModelAdmin):
   list_display = (
        'header_styling',
        'do_not_display',
    )
   list_editable = (
        'do_not_display',
       
   )


class ProductsPageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'products_page_styling',
        'do_not_display',
    )
    list_editable = (
            'do_not_display',
        
    )
    
"""
superadmin.register() to register for superuser admin
"""

superadmin.register(HomePageCustomisation, HomePageCustomisationAdmin)
superadmin.register(HeaderCustomisation, HeaderCustomisationAdmin)
superadmin.register(ProductsPageCustomisation, ProductsPageCustomisationAdmin)
