from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    """Homepage: show all recipes by category"""
    recipes = Recipe.objects.all().order_by('category', 'title')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)

def recipe_detail(request, recipe_id):
    """Show details for a single recipe"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)

