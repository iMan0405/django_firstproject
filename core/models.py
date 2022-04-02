from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)