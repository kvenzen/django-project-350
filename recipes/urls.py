from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),                # Homepage: list all recipes
    path('add/', views.add_recipe, name='add_recipe'),  # Add a new recipe
    path('dashboard/', views.dashboard, name='dashboard'),     #  dashboard page
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Recipe detail
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('categories/', views.categories_overview, name='categories'),   # Categories overview
]

