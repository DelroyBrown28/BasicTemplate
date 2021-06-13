from django.contrib import admin
from django.contrib.sites.models import Site
# from taggit.admin import Tag
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from products.models import Product
from .models import HomePageSuperuserAdmin
# from wagtail.images.models import Image
# from wagtail.documents.models import Document


class HomepageSuperuserAdmin(admin.ModelAdmin):
    model = HomePageSuperuserAdmin
    
    list_display = (
        'background_image',
    )


admin.site.register(HomePageSuperuserAdmin)
admin.site.unregister(Site)
# admin.site.unregister(Tag)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
# admin.site.unregister(Document)
# admin.site.unregister(Image)

