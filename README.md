Kitcher Restaurant Management System
Kitcher Restaurant Management System is a web application designed to manage restaurant operations, including managing cooks, dishes, and ingredients. This application is built using Django, a high-level Python web framework.
use 
```
use python manage.py loaddata kitcherapp_data.json
admin user: "admin"
admin password: "123123admin"
```
Features
User Authentication: Login and logout functionalities.
Cook Management: Add, edit, and view details of cooks. Includes superuser functionality for administrative tasks.
Dish Management: Add, edit, and view details of dishes, including assigning cooks and ingredients to each dish.
Ingredient Management: Manage ingredients used in dishes.
Search and Pagination: Easily search for cooks and dishes with pagination support.
Installation
Clone the repository:
python manage.py runserver
Usage
Navigate to the application:
Open your web browser and go to http://127.0.0.1:8000/.

Login:
Use the credentials created during the superuser setup to login.

Manage Cooks:

Add new cooks.
View, edit, and delete existing cooks.
Search for cooks by name or job title.
Manage Dishes:

Add new dishes.
View, edit, and delete existing dishes.
Assign cooks and ingredients to each dish.
Search for dishes by name or type.
Manage Ingredients:

Add new ingredients.
View, edit, and delete existing ingredients.
Models
Cook
Represents a cook working in the restaurant.

first_name: First name of the cook.
last_name: Last name of the cook.
phone: Contact phone number of the cook.
address: Address of the cook.
year_of_experience: Years of experience the cook has.
job_title: Job title of the cook (e.g., Chef, Sous Chef).
DishType
Represents different types of dishes (e.g., Appetizer, Main Course, Dessert).

name: Name of the dish type.
Dish
Represents a dish served in the restaurant.

name: Name of the dish.
description: Description of the dish.
price: Price of the dish.
dish_type: Type of the dish.
cooks: Cooks who can prepare this dish.
ingredients: Ingredients used in this dish.
Ingredient
Represents an ingredient used in dishes.

name: Name of the ingredient.
description: Description of the ingredient (optional).
