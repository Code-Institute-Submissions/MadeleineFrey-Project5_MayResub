from django.db import models

# Create your models here.

class AboutUs(models.Model):
    """ X """

    name = models.CharField(max_length=60)
    description = models.TextField()
    years = models.DecimalField(max_digits=6, decimal_places=2)
    profile_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name