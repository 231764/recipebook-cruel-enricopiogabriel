# ledger/views.py
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_details.html'


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    # template_name = '<model>task_form.html'
    template_name = 'recipe_details.html'
    form_class = RecipeImageForm

    def get_success_url(self):
        return f"/recipe/{self.kwargs['pk']}"  # redirect back to detail page

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    # template_name = '<model>task_form.html'
    template_name = 'recipe_details.html'
    form_class = RecipeForm


def add_recipe(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('ledger:recipes-list'))
        else:
            form = RecipeForm()
            
    ctx = {'form': form}

    return render(request, 'add_recipe.html', ctx)

def add_image(request, pk):
    form = RecipeImageForm()
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('ledger:recipe-detail', args=[pk]))
        else:
            form = RecipeImageForm()
            
    ctx = {
        'form': form,
        'object': recipe
           }

    return render(request, 'add_forms.html', ctx)


# Create your views here.

