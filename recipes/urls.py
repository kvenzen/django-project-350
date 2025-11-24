from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),  # Homepage: list of all recipes
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Detail view for a single recipe
]


