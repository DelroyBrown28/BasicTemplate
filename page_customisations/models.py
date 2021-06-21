from django.db import models
from colorfield.fields import ColorField



class HomePageCustomisation(models.Model):
    TEXT_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    BUTTON_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    home_page_styling = models.CharField(blank=False, null=False, max_length=35, default="Name This Styling...")
    image = models.ImageField(null=True, blank=True)
    main_page_text = models.TextField(blank=False, null=False)
    main_page_text_alignment = models.TextField(choices=TEXT_ALIGNMENT_CHOICES,blank=False, null=False, default='text-align__left')
    main_page_text_color = ColorField(format='hexa')
    button_text = models.CharField(blank=False, null=False, max_length=15, default='Shop Now')
    button_text_color = ColorField(format='hexa')
    button_background_color = ColorField(format='hexa')
    main_page_button_alignment = models.TextField(choices=BUTTON_ALIGNMENT_CHOICES,blank=False, null=False, default='text-align__left')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                        default=False,
                                        help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')

    
    class Meta:
        verbose_name_plural = 'Home Page'
        
    
    def __str__(self):
        return self.home_page_styling
    

class HeaderCustomisation(models.Model):
    header_styling = models.CharField(blank=False, null=False, max_length=55, default="Default Styling")
    header_logo = models.ImageField(null=True, blank=True, upload_to='media')
    header_background_color = ColorField(format='hexa')
    header_icon_color = ColorField(format='hexa')
    header_text_color = ColorField(format='hexa')
    search_icon_color = ColorField(format='hexa')
    search_icon_background_color = ColorField(format='hexa')
    small_banner_text = models.CharField(blank=False, null=False, max_length=100, default="Welcome")
    small_banner_background_color = ColorField(format='hexa')
    small_banner_text_color = ColorField(format='hexa')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')
    
    class Meta:
        verbose_name_plural = 'Header'
        
    
    def __str__(self):
        return self.header_styling
 
    
class ProductsPageCustomisation(models.Model):
    BORDER_SIZE_CHOICES = (
        ('add-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    products_page_styling = models.CharField(blank=False, null=False, max_length=55, default="Default Product Page Styling")
    add_card_border = models.TextField(choices=BORDER_SIZE_CHOICES,
                                                   blank=False,
                                                   null=False,
                                                   default="No Border")
    border_color = ColorField(format='hexa')
    product_card_font_color = ColorField(format='hexa')
    product_card_icon_color = ColorField(format='hexa')
    
    
    class Meta:
        verbose_name_plural = 'Products Page'
        
    
    def __str__(self):
        return self.products_page_styling