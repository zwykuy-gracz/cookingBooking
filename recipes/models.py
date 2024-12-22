from django.db import models

# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # dishes = models.ManyToManyField("recipes.Dish", blank=True, related_name="dishes")

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dishes")
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    recipe = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    food_tags = models.ManyToManyField("recipes.Tag")  # , related_name="dishes")

    def __str__(self) -> str:
        return self.title
