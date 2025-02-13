# ledger/urls.py
from django.urls import path
from .views import index, recipes_list, recipe_1, recipe_2

urlpatterns = [
        path('', index, name='index'),
        path('recipes/list', recipes_list, name='recipes/list'),
        path('recipe/1', recipe_1, name='recipes/1'),
        path('recipe/2', recipe_2, name='recipes/2'),

]

# This might be needed, depending on your Django version
app_name = "ledger"