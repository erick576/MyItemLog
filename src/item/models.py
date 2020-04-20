from django.db import models


# Create your models here.
class entry(models.Model):
    Item = models.CharField(blank=False, max_length=120)
    Picture = models.ImageField(blank=True, null=True, upload_to="covers/%Y/%m/%D/", height_field=100, width_field=100)
    Description = models.TextField(blank=True)
    Price = models.DecimalField(blank=True, max_digits=100, decimal_places=2)
    Date = models.DateField(blank=True)
    URL = models.URLField(blank=True, max_length=200)
    Comments = models.TextField(blank=True)
