from django.db import models


class HomePageCustomisation(models.Model):
    image_title_for_backend = models.CharField(blank=False, null=False, max_length=35, default="image title...")
    image = models.ImageField(null=True, blank=True)
    main_page_text = models.TextField(blank=False, null=False, max_length=3500)
    button_text = models.TextField(blank=False, null=False, max_length=15, default='Shop Now')
    
    class Meta:
        verbose_name_plural = 'Home Page Customisation'
        
    
    def __str__(self):
        return self.image_title_for_backend
    

class HeaderCustomisation(models.Model):
    BACKGROUND_COLOR_CLASS_CHOICES = (
        ('admin-bg-color__red', 'Red'),
        ('admin-bg-color__blue', 'Blue'),
        ('admin-bg-color__green', 'Green'),
        ('admin-bg-color__black', 'Black'),
        ('admin-bg-color__white', 'White'),
    )
    TEXT_COLOR_CLASS_CHOICES = (
        ('admin-color__red', 'Red'),
        ('admin-color__blue', 'Blue'),
        ('admin-color__green', 'Green'),
        ('admin-color__black', 'Black'),
        ('admin-color__white', 'White'),
    )
    
    small_banner_text = models.CharField(blank=False, null=False, max_length=200, default="Welcome")
    choose_background_color_class = models.CharField(choices=BACKGROUND_COLOR_CLASS_CHOICES, blank=False, null=False, max_length=30, default="Blue")
    choose_text_color_class = models.CharField(choices=TEXT_COLOR_CLASS_CHOICES, blank=False, null=False, max_length=30, default="Blue")
    
    class Meta:
        verbose_name_plural = 'Header Customisation'
        
    
    def __str__(self):
        return self.small_banner_text
    
    