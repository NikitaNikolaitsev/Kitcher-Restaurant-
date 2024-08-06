from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    year_of_experience = models.IntegerField(default=0)
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.job_title} {self.first_name} {self.last_name}"

    class Meta:
        ordering = ("job_title",)

    def get_absolute_url(self):
        return reverse('kitcher:staff-detail', kwargs={'pk': self.pk})


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, blank=True, related_name="dishes")
    ingredients = models.ManyToManyField("Ingredient", related_name='dishes', blank=True)

    class Meta:
        ordering = ("dish_type",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitcher:dish-detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
