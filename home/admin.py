from django.contrib import admin
from django.contrib.sites.models import Site
# from taggit.admin import Tag
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from products.models import Product
from .models import HomePageCustomisation



class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'image_title_for_backend',
    )



admin.site.register(HomePageCustomisation, HomePageCustomisationAdmin)
admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)

