from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # to allow adding extra RecipeIngredients

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)  # Allow searching by author
    list_display = ('name',)  
    list_filter = ('name', 'ingredients',)  
    inlines = [RecipeIngredientInline, RecipeImageInline]  # Allows editing RecipeIngredients in Recipe Admin

    fieldsets = [
        ('Recipe Information', {
            'fields': ['name', 'author',],
        }),
    ]
class IngredientAdmin(admin.ModelAdmin): 
    model = Ingredient
    list_display = ('name',) 
    search_fields = ('name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
