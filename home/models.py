from django.db import models
from djrichtextfield.models import RichTextField


class HomePageCustomisation(models.Model):
    image_title_for_backend = models.CharField(blank=False, null=False, max_length=35, default="image title...")
    image = models.ImageField(upload_to='media')
    main_page_text = RichTextField()
    
    def __str__(self):
        return self.image_title_for_backend

