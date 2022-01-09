from django.db import models
from django.db.models.fields import CharField
from django.db.models.lookups import Regex

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    reg = models.IntegerField() 
    dep = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

  
