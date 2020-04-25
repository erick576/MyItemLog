from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.urls import reverse


class entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Item = models.CharField(blank=False, max_length=120, null=False)
    Picture_URL = models.URLField(blank=True, max_length=2000, null=True)
    Description = models.TextField(blank=True, null=False)
    Price = models.DecimalField(blank=True, max_digits=100, decimal_places=2, null=True)
    Date = models.DateField(blank=True, null=True)
    URL = models.URLField(blank=True, max_length=200, null=True)

    def get_absolute_url_delete(self):
        return reverse("delete-item", kwargs={"id": self.id})

    def get_absolute_url_edit(self):
        return reverse("edit-item", kwargs={"id": self.id})
