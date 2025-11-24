from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50, blank=True)  # e.g., Main, Side, Dessert, Drink
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

