from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from kitcherapp.models import Cook


def validate_name(name: str, name_type: str = "name"):
    if len(name) < 3 or len(name) > 20:
        raise ValidationError(f"Enter a valid {name_type}")
    if not name[0].isalpha():
        raise ValidationError(f"Enter a valid {name_type}")
    if isinstance(name, int):
        raise ValidationError(f"Enter a valid {name_type}")


def validate_years_of_experience(years: int):
    if years < 0:
        raise ValidationError("Years of experience must be a positive number")


class CookCreateForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "years_of_experience", "phone", "address")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        validate_name(first_name, "first name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        validate_name(last_name, "last name")
        return last_name

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        validate_years_of_experience(years_of_experience)
        return years_of_experience
