from django.test import TestCase
from .models import Cook, Dish, DishType, Ingredient


class CookModelTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create(
            username='jdoe',
            first_name='John',
            last_name='Doe',
            phone='123-456-7890',
            address='123 Elm Street',
            year_of_experience=5,
            job_title='Chef'
        )

    def test_cook_creation(self):
        self.assertTrue(isinstance(self.cook, Cook))
        self.assertEqual(self.cook.username, 'jdoe')
        self.assertEqual(self.cook.first_name, 'John')
        self.assertEqual(self.cook.last_name, 'Doe')
        self.assertEqual(self.cook.phone, '123-456-7890')
        self.assertEqual(self.cook.address, '123 Elm Street')
        self.assertEqual(self.cook.year_of_experience, 5)
        self.assertEqual(self.cook.job_title, 'Chef')

    def test_string_representation(self):
        self.assertEqual(str(self.cook), 'Chef John Doe')

    def test_ordering(self):
        cook2 = Cook.objects.create(
            username='asmith',
            first_name='Alice',
            last_name='Smith',
            phone='987-654-3210',
            address='456 Oak Avenue',
            year_of_experience=3,
            job_title='Sous Chef'
        )
        self.assertEqual(list(Cook.objects.all()), [self.cook, cook2])


class DishModelTests(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name="Soup")
        self.ingredient = Ingredient.objects.create(name="Tomato")

        self.cook = Cook.objects.create(
            username='jdoe',
            first_name='John',
            last_name='Doe',
            phone='123-456-7890',
            address='123 Elm Street',
            year_of_experience=5,
            job_title='Chef'
        )

        self.dish = Dish.objects.create(
            name="borsh",
            description="very testy borsh",
            price=12.99,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_string_representation(self):
        self.assertEqual(str(self.dish), "borsh")


class DishTypeModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Soup")

    def test_dish_type_creation(self):
        self.assertTrue(isinstance(self.dish_type, DishType))
        self.assertEqual(self.dish_type.name, "Soup")

    def test_dish_type_string_representation(self):
        self.assertEqual(str(self.dish_type), "Soup")


class IngredientModelTests(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name="Tomato",
            description="very testy tomato",
        )

    def test_ingredient_creation(self):
        self.assertTrue(isinstance(self.ingredient, Ingredient))
        self.assertEqual(self.ingredient.name, "Tomato")

    def test_ingredient_string_representation(self):
        self.assertEqual(str(self.ingredient), "Tomato")
