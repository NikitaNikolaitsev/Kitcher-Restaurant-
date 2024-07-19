from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    year_of_experience = models.IntegerField()
    job_title = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='cooks'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='cooks'
    )

    def __str__(self):
        return f"{self.job_title} {self.first_name} {self.last_name}"

    class Meta:
        ordering = ("job_title",)


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    job_title = models.ForeignKey(Cook, on_delete=models.CASCADE, related_name='dish_types')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, blank=True, related_name="dishes")

    def __str__(self):
        return self.name
