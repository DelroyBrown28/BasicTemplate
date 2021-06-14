from django.contrib import admin
from django.contrib.sites.models import Site
# from taggit.admin import Tag
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from products.models import Product
from .models import HomePageCustomisation
# from wagtail.images.models import Image
# from wagtail.documents.models import Document



admin.site.register(HomePageCustomisation)
admin.site.unregister(Site)
# admin.site.unregister(Tag)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
# admin.site.unregister(Document)
# admin.site.unregister(Image)

