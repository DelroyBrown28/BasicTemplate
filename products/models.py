from django.db import models
from django import forms


class Category(models.Model):
    
    class Meta:
        verbose_name = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=False, null=False)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
        
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
# class ProductsPageCustomisation(models.Model):
#     BORDER_COLOR_CHOICES = (
#         ('add-border__red', 'Red'),
#         ('add-border__blue', 'Blue'),
#         ('add-border__green', 'Green'),
#         ('add-border__black', 'Black'),
#         ('add-border__white', 'White'),
#         ('no-border', 'No Border'),
#     )
#     name_these_changes = models.CharField(blank=False, null=False, max_length=200, default="Default Product Page Styling")
#     choose_border_color = models.CharField(choices=BORDER_COLOR_CHOICES, blank=False, null=False, max_length=30, default="No Border")
    
#     class Meta:
#         verbose_name_plural = 'Products Page Customisation'
        
    
#     def __str__(self):
#         return self.name_these_changes
    
    