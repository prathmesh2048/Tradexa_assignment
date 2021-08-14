from django.db import models
from django.db.models.fields import CharField
import datetime
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveBigIntegerField(null=True)
    price = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(),blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True) 


    def __str__(self):
        return self.name
    