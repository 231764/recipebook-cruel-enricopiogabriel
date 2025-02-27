from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # to allow adding extra RecipeIngredients

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [RecipeIngredientInline]  # allows editing RecipeIngredients in Recipe Admin

    fieldsets = [
        ('Recipe Information', {
            'fields': ['name'],
        }),
    ]

admin.site.register(Recipe, RecipeAdmin)
