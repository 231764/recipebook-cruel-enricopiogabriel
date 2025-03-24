from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): 
        return reverse('ledger:recipe', args=[self.pk]) 

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        null=True,
        blank=True)
    created_on = models.DateTimeField(auto_now_add=True)  # Sets date and time on creation
    updated_on = models.DateTimeField(auto_now=True)  # Updates date and time on save

    def __str__(self): 
        return self.name
        
    def get_absolute_url(self): 
        return reverse('ledger:recipe-detail', args=[self.pk]) 

class RecipeImage(models.Model):
    image = models.ImageField(null=True, upload_to='images/')
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images'
    )


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='recipe'
    ) 
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='ingredients'
    ) 


# Create your models here.
