from django.db import models


class HomePageCustomisation(models.Model):
    TEXT_COLOR_CLASS_CHOICES = (
        ('admin-color__red', 'Red'),
        ('admin-color__blue', 'Blue'),
        ('admin-color__green', 'Green'),
        ('admin-color__black', 'Black'),
        ('admin-color__white', 'White'),
    )
    BACKGROUND_COLOR_CLASS_CHOICES = (
        ('admin-bg-color__red', 'Red'),
        ('admin-bg-color__blue', 'Blue'),
        ('admin-bg-color__green', 'Green'),
        ('admin-bg-color__black', 'Black'),
        ('admin-bg-color__white', 'White'),
    )
    name_these_changes = models.CharField(blank=False, null=False, max_length=35, default="Name This Styling...")
    image = models.ImageField(null=True, blank=True)
    main_page_text = models.TextField(blank=False, null=False, max_length=3500)
    main_page_text_color = models.TextField(choices=TEXT_COLOR_CLASS_CHOICES, default='Pick a color')
    button_text = models.CharField(blank=False, null=False, max_length=15, default='Shop Now')
    button_text_color = models.TextField(choices=TEXT_COLOR_CLASS_CHOICES, default='Pick a color')
    button_background_color = models.CharField(choices=BACKGROUND_COLOR_CLASS_CHOICES, blank=False, null=False, max_length=30, default="Blue")
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                        default=False,
                                        help_text='Check this box to hide this specific banner.')

    
    class Meta:
        verbose_name_plural = 'Home Page Customisation'
        
    
    def __str__(self):
        return self.name_these_changes
    

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
    name_these_changes = models.CharField(blank=False, null=False, max_length=200, default="Default Styling")
    small_banner_text = models.CharField(blank=False, null=False, max_length=200, default="Welcome")
    choose_background_color_class = models.CharField(choices=BACKGROUND_COLOR_CLASS_CHOICES, blank=False, null=False, max_length=30, default="Blue")
    choose_text_color_class = models.CharField(choices=TEXT_COLOR_CLASS_CHOICES, blank=False, null=False, max_length=30, default="Blue")
    header_logo = models.ImageField(null=True, blank=True, upload_to='media')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='Check this box to hide this specific banner.')
    
    class Meta:
        verbose_name_plural = 'Header Customisation'
        
    
    def __str__(self):
        return self.name_these_changes
    
    