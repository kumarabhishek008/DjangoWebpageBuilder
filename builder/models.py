from django.db import models

# Create your models here.
class Pages(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    preview_link = models.TextField()

