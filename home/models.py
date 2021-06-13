from django.db import models


class HomePageSuperuserAdmin(models.Model):
    background_image = models.ImageField(upload_to='media')
    
 
