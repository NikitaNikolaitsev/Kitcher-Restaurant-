from django.test import TestCase
from .models import Cook


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
