from django.db import models

from products.models import Product

class Order(models.Model):
    """ Order with street_address2 and county Blank """
    full_name = models.CharField(max_length=50, blank=False, help_text="Enter full name of individual (e.g. Joe Bloggs) or Business (e.g. Facebook)")
    phone_number = models.CharField(max_length=20, blank=False, help_text="Enter phone number (can be landline or mobile)")
    country = models.CharField(max_length=40, blank=True, help_text="Enter name of country (e.g. United Kingdom)")
    postcode = models.CharField(max_length=20, blank=True, help_text="Enter postcode (e.g. BR1 3ES)")
    town_or_city = models.CharField(max_length=40, blank=False, help_text="Enter name of town or city (e.g. March, Peterborough)")
    street_address1 = models.CharField(max_length=40, blank=False, help_text="Enter first line of home or business address")
    street_address2 = models.CharField(max_length=40, blank=True, help_text="Enter second line of home or business address (optional)")
    county = models.CharField(max_length=40, blank=True, help_text="Enter name of county (e.g. Cambs or Cambridgeshire).  This field is optional.")
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
