# ledger/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import RecipeIngredient, Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_details.html'

def index(request):
    return HttpResponse('Hello World! This ma recipe')

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
    "recipes": recipes
    }

    return render(request, 'recipes_list.html', ctx)

def recipe(request):
    recipe = RecipeIngredient.objects.all()
    ctx = {
        "recipe": recipe
    }
    return render(request, 'recipe_details.html', ctx)

# Create your views here.

