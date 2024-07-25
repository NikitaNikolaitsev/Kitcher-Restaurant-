Here's the revised README for the Kitcher Restaurant Management System in English:

---

# Kitcher Restaurant Management System

Kitcher Restaurant Management System is a web application designed to manage restaurant operations, including managing cooks, dishes, and ingredients. This application is built using Django, a high-level Python web framework.

## Load Prepared Data

To load prepared data, use the following command:
```bash
python manage.py loaddata kitcherapp_data.json
```
Admin user:
- Username: "troll_admin"
- Password: "123123admin"

## Features

- **User Authentication:** Login and logout functionalities.
- **Cook Management:** Add, edit, and view details of cooks. Includes superuser functionality for administrative tasks.
- **Dish Management:** Add, edit, and view details of dishes, including assigning cooks and ingredients to each dish.
- **Ingredient Management:** Manage ingredients used in dishes.
- **Search and Pagination:** Easily search for cooks and dishes with pagination support.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NikitaNikolaitsev/Kitcher-Restaurant-.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Navigate to the Application:
1. Open your web browser and go to http://127.0.0.1:8000/.

### Login:
1. Use the credentials created during the superuser setup to log in.

### Manage Cooks:
1. Add new cooks.
2. View, edit, and delete existing cooks.
3. Search for cooks by name or job title.

### Manage Dishes:
1. Add new dishes.
2. View, edit, and delete existing dishes.
3. Assign cooks and ingredients to each dish.
4. Search for dishes by name or type.

### Manage Ingredients:
1. Add new ingredients.
2. View, edit, and delete existing ingredients.

## Models

### Cook
Represents a cook working in the restaurant.
- `first_name`: First name of the cook.
- `last_name`: Last name of the cook.
- `phone`: Contact phone number of the cook.
- `address`: Address of the cook.
- `year_of_experience`: Years of experience the cook has.
- `job_title`: Job title of the cook (e.g., Chef, Sous Chef).

### DishType
Represents different types of dishes (e.g., Appetizer, Main Course, Dessert).
- `name`: Name of the dish type.

### Dish
Represents a dish served in the restaurant.
- `name`: Name of the dish.
- `description`: Description of the dish.
- `price`: Price of the dish.
- `dish_type`: Type of the dish.
- `cooks`: Cooks who can prepare this dish.
- `ingredients`: Ingredients used in this dish.

### Ingredient
Represents an ingredient used in dishes.
- `name`: Name of the ingredient.
- `description`: Description of the ingredient (optional).

---
