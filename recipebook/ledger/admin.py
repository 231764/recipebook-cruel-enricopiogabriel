from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # Allows adding extra RecipeIngredients directly from Recipe admin

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [RecipeIngredientInline]  # Allows editing RecipeIngredients in Recipe admin

    fieldsets = [
        ('Recipe Information', {
            'fields': ['name'],
        }),
    ]

admin.site.register(Recipe, RecipeAdmin)
