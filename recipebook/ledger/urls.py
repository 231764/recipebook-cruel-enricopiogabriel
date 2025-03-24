# ledger/urls.py
from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, add_image, add_recipe

urlpatterns = [
        path('recipes/list', RecipeListView.as_view(), name='recipes-list'),
        path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
        path('recipe/<int:pk>/add_image', add_image, name='add-image'),
        path('recipe/add', add_recipe, name='recipe-create')
]

app_name = "ledger"