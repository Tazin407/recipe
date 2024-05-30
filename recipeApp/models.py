from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredients(models.model):
    name= models.CharField(max_length=30)
    
class Recipe(models.Model):
    name= models.CharField(max_length=30)
    ingredient= models.ManyToManyField(Ingredients)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    description= models.TextField()

