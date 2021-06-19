from django.contrib import admin
from django.contrib.sites.models import Site
# from taggit.admin import Tag
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from products.models import Product, Category
from checkout.models import Order, OrderLineItem
# from page_customisations.models import HomePageCustomisation, HeaderCustomisation
# from products.models import ProductsPageCustomisation
from BasicTemplateMain.admin import superadmin


# Superuser admin models
class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'name_these_changes',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',
       
    )

    
class HeaderCustomisationAdmin(admin.ModelAdmin):
   list_display = (
        'name_these_changes',
        'do_not_display',
    )
   list_editable = (
        'do_not_display',
       
   )


class ProductsPageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'name_these_changes',
    )

# Store owners admin models     
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )
    fields = (
        'full_name',
        'user_profile',
        'order_number',
        'date',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )
    list_display = (
        'full_name',
        'date',
        'order_total',
        'delivery_cost',
        'grand_total',
        'order_number',
    )
    search_fields = [
        'full_name',
        'date',
        'order_number',
    ]
    ordering = ('-date',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )
    search_fields = [
        'name',
        'sku',
        'price',
    ]
    list_filter = (
        'name',
        'category',
    )

    ordering = ('name',)    

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    list_display_links = ('name',)
    list_editable = (
        'friendly_name',
    )



admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)

