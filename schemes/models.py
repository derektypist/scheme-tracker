from django.db import models
from django.utils import timezone

class Scheme(models.Model):
    """ Scheme Post with help text """
    title = models.CharField(max_length=100, help_text="Enter scheme title (e.g. Ely Southern Bypass)")
    description = models.TextField(help_text="Enter description of scheme (e.g. The Ely Southern Bypass is designed to Reduce Bridge Strikes)")
    comment = models.TextField(help_text="Enter a comment.  You can include what has been done and what needs to be doing, such as Building Works have been completed, now needs to comply with Health & Safety Requirements.  Or you can just include feedback with or without further actions, such as Good Work.")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    completion = models.DecimalField(max_digits=3, decimal_places=2, help_text="Enter a percentage, (e.g. 25 for Partially Complete or 100 for Complete)")
    image = models.ImageField(upload_to='images')
    
    def __unicode__(self):
        return self.title   