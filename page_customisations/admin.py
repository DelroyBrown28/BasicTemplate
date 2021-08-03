from django.contrib import admin
from django.contrib.auth.models import User
from page_customisations.models import (HomePageCustomisation,
                                        HeaderCustomisation,
                                        ProductsPageCustomisation,
                                        GlobalSiteStyling,
                                        AboutPageCustomisation)
from BasicTemplateMain.admin import superadmin


# Superuser admin models
class HomePageCustomisationAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                "fields": (
                    'home_page_styling',
                    'image',)
            }),
            
                ('Main Text', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'main_page_text',
                        'main_page_text_alignment',
                        'main_page_text_color'),
            
            }),
                ('Button Styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'button_text',
                        'button_text_color',
                        'button_background_color',
                        'main_page_button_alignment',),
            
            }),
                ('Tick this box to HIDE these styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'do_not_display',),
            }),
        )
        list_display = (
            'home_page_styling',
            'do_not_display',
        )
        list_editable = (
            'do_not_display',
        
        )
    
class GlobalSiteStylingAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                "fields": (
                    'global_site_styles',
                    'base_background_color',
                    'base_font_color',
                    'all_icon_colors',)
            }),
                ('Primary Button Styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                            ('primary_button_base_color',
                            'primary_button_text_color'),)
            
            }),
                ('Secondary Button Styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        ('secondary_button_base_color',
                        'secondary_button_text_color'),)
            
            }),
                ('Pop up box styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        ('pop_up_background_color',
                        'pop_up_text_color'),)
            }),
        
                ('Tick this box to HIDE these styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'do_not_display',),
            }),
        )
        list_display = (
            'global_site_styles',
            'do_not_display',
        )
        list_editable = (
            'do_not_display',
        
        )

    
class HeaderCustomisationAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                "fields": (
                    'header_styling',
                    'header_logo',
                    'header_background_color',)
            }),
                ('Search icon and icon background', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                            ('search_icon_color',
                            'search_icon_background_color'),)
            
            }),
                ('Small Banner', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'small_banner_text',
                        ('small_banner_background_color',
                        'small_banner_text_color',),)
            
            }),
                
                ('Tick this box to HIDE these styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'do_not_display',),
            }),
        )
        list_display = (
                'header_styling',
                'do_not_display',
            )
        list_editable = (
                'do_not_display',
            
        )


class ProductsPageCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                "fields": (
                    'products_page_styling',)
            }),
                ('Category Tag', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                            ('category_tag_border_color',
                            'category_tag_text_color'),)
            
            }),
                ('Product Cards', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'product_card_background_color',
                        ('add_card_border',
                        'border_color'),
                        'product_card_font_color',
                        'product_card_icon_color',),
            
            }),  
                ('Tick this box to HIDE these styles', {
                    'classes': ('fieldset_titles',),
                    'fields': (
                        'do_not_display',),
            }),
        )
    list_display = (
        'products_page_styling',
        'do_not_display',
    )
    list_editable = (
            'do_not_display',
        
    )
    
class AboutPageCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'styling_name',)
        }),
            ('About Section', {
                'classes': ('fieldset_titles',),
                'fields': (
                        'about_section_title',
                        'about_section_blurb',
                        'about_section_content',
                        'about_section_left_image',
                        'about_section_right_image'),
        
        }),
            ('Contact Section', {
                'classes': ('fieldset_titles',),
                'fields': (
                    'contact_section_title',
                    'contact_section_blurb',)
        
        }),
            ('Contact Card', {
                'classes': ('fieldset_titles',),
                'fields': (
                    'contact_card_title',
                    'contact_card_image',
                    'contact_card_info'),
        
        }),
            ('Social Media Links', {
                'classes': ('fieldset_titles',),
                'fields': (
                    ('twitter_link',
                    'linkedin_link'),
                    ('facebook_link',
                    'instagram_link'),),
        }),
    
            ('Tick this box to HIDE these styles', {
                'classes': ('fieldset_titles',),
                'fields': (
                    'do_not_display',),
        }),
    )
    list_display = (
    'styling_name',
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
superadmin.register(GlobalSiteStyling, GlobalSiteStylingAdmin)
superadmin.register(AboutPageCustomisation, AboutPageCustomisationAdmin)
superadmin.register(User)
