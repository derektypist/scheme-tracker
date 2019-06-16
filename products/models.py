from django.db import models

# Create your models here.
class Product(models.Model):
    """ Define Product """
        
    # Select Box for CATEGORIES
    CATEGORIES = (
        ('Ga', 'Garden'),
        ('He', 'Health & Safety'),
        ('I', 'IT'),
        ('Li', 'Lighting'),
        ('Ot', 'Other')
    )
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    category_type = models.CharField(max_length=2, choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name