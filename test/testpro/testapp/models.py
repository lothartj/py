from django.db import models

# Create your models here.
class Items(models.Model):
    itemno = models.CharField(max_length=50)
    itemdescription = models.CharField(max_length=50)
    itembarcode = models.CharField(max_length=50)
    itemuom = models.CharField(max_length=50)
  