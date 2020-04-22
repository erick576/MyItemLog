from django.db import models


# Create your models here.
class entry(models.Model):
    Item = models.CharField(blank=False, max_length=120)
    Picture_URL = models.CharField(blank=True, max_length=2000)
    Description = models.TextField(blank=True)
    Price = models.DecimalField(blank=True, max_digits=100, decimal_places=2)
    Date = models.DateField(blank=True)
    URL = models.URLField(blank=True, max_length=200)
