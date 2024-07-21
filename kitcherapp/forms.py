from decimal import Decimal

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

from kitcherapp.models import Cook, Dish, DishType


def validate_name(name: str):
    if len(name) < 3 or len(name) > 20:
        raise ValidationError(f"Enter a valid name")
    if not isinstance(name, str):
        raise ValidationError(f"Enter a valid name")


def validate_years_of_experience(years: int):
    if years < 0 or years > 100:
        raise ValidationError("Please enter valid years")


class CookCreateForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "year_of_experience", "job_title", "address", "phone")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        validate_name(first_name, "first name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        validate_name(last_name, "last name")
        return last_name

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("year_of_experience")
        validate_years_of_experience(years_of_experience)
        return years_of_experience


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ("name", "description", "price",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return validate_name(name)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if not isinstance(price, (int, float, Decimal)) or price <= 0:
            raise ValidationError("Please enter a valid price")
        return price


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ("name",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return validate_name(name)


"""
SEARCH FORMS
"""


class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Dish Name')
    min_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Min Price')
    max_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Max Price')


class CookSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Cook Name')
    job_title = forms.CharField(max_length=100, required=False, label='Job Title')
