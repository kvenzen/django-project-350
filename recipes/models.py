from django.db import models

class Category(models.Model):
    """Recipe category, e.g., Main Dish, Dessert, etc."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """A single recipe."""
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='recipes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    """Ingredients for a recipe."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"

