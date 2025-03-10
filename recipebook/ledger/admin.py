from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin): 
    inlines = [ProfileInline,]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # to allow adding extra RecipeIngredients

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author__username')  # Allow searching by author
    list_display = ('name', 'author', 'created_on', 'updated_on')  
    list_filter = ('name', 'author', 'created_on', 'updated_on')  
    inlines = [RecipeIngredientInline]  # Allows editing RecipeIngredients in Recipe Admin

    fieldsets = [
        ('Recipe Information', {
            'fields': ['name', 'author',],
        }),
    ]
class IngredientAdmin(admin.ModelAdmin): 
    model = Ingredient
    list_display = ('name',) 
    search_fields = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'short_bio')
    search_fields = ('user__username', 'short_bio')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)