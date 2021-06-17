from django.db import models


class HomePageCustomisation(models.Model):
    image_title_for_backend = models.CharField(blank=False, null=False, max_length=35, default="image title...")
    image = models.ImageField(null=True, blank=True)
    main_page_text = models.TextField(blank=False, null=False, max_length=3500)
    
    class Meta:
        verbose_name_plural = 'Home Page Customisation'
        
    
    def __str__(self):
        return self.image_title_for_backend
    

class HeaderCustomisation(models.Model):
    small_banner_text = models.CharField(blank=False, null=False, max_length=200, default="Welcome")
    
    class Meta:
        verbose_name_plural = 'Header Customisation'
        
    
    def __str__(self):
        return self.small_banner_text
    
    