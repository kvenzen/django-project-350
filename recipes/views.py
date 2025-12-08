from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Recipe, Category, Ingredient

def index(request):
    recipes = Recipe.objects.all().order_by('category__name', 'title')
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)


def categories_overview(request):
    categories = Category.objects.annotate(num_recipes=Count('recipes')).order_by('name')
    context = {'categories': categories}
    return render(request, 'recipes/categories.html', context)


def dashboard(request):
    categories_count = Category.objects.count()
    recipes_count = Recipe.objects.count()
    context = {
        'categories_count': categories_count,
        'recipes_count': recipes_count,
    }
    return render(request, 'recipes/stats.html', context)


def add_recipe(request):
    categories = Category.objects.all()  # all categories

    if request.method == 'POST':
        title = request.POST.get('title')
        instructions = request.POST.get('instructions')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id) if category_id else None

        recipe = Recipe.objects.create(
            title=title,
            instructions=instructions,
            category=category  # assign the actual Category object
        )

        # Add ingredients
        ingredient_names = request.POST.getlist('ingredient_name')
        quantities = request.POST.getlist('ingredient_quantity')
        units = request.POST.getlist('ingredient_unit')

        for i in range(len(ingredient_names)):
            name = ingredient_names[i]
            qty = quantities[i]
            unit = units[i]
            if name.strip():
                Ingredient.objects.create(
                    recipe=recipe,
                    name=name,
                    quantity=float(qty),
                    unit=unit
                )

        return redirect('recipes:index')

    context = {'categories': categories}
    return render(request, 'recipes/add_recipe.html', context)

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        recipe.delete()
        return redirect('recipes:index')

    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})

