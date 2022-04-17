from django.db import models

class Category(models.Model):
    """ Model to store different Categories"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Box(models.Model):
    """ X """

    class Meta:
        """ X """
        
        verbose_name_plural = 'Boxes'

    name = models.CharField(max_length=60)
    sku = models.CharField(max_length=12, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name