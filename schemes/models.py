from django.db import models
from django.utils import timezone

class Scheme(models.Model):
    """ Scheme Post """
    title = models.CharField(max_length=100, help_text="Enter scheme title (e.g. Ely Southern Bypass)")
    description = models.TextField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    completion = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __unicode__(self):
        return self.title   