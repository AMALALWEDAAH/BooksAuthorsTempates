from django.db import models
from urllib import request
# Create your models here.
class Authors(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    notes= models.CharField(max_length=255)

class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default='')
    uploaded_by = models.ManyToManyField(Authors, related_name="Books")