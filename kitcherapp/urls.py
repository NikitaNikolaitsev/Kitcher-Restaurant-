from django.urls import path
from kitcherapp import views
from kitcherapp.views import (
    index,
    MenuView,
    MenuUpdateView,
    MenuDeleteView,
    MenuCreateView,
    StaffBaseView,
    StaffDetailView,
    StaffUpdateView,
    StaffDeleteView,
    StaffCreateView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishDetailView,
    IngredientUpdateView,
    IngredientCreateView,
    home,
    dish_search,
    cook_search,
)

app_name = "kitcher"

urlpatterns = [
    path("", index, name="index"),

    path("menu/", MenuView.as_view(), name="menu"),
    path("menu/create/", MenuCreateView.as_view(), name="menu-create"),
    path("menu/<int:pk>/update/", MenuUpdateView.as_view(), name="menu-update"),
    path("menu/<int:pk>/delete/", MenuDeleteView.as_view(), name="menu-delete"),
    path("menu/<int:pk>/detail/", DishDetailView.as_view(), name="dish-detail"),

    path("staff/", StaffBaseView.as_view(), name="staff"),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("staff/<int:pk>/update/", StaffUpdateView.as_view(), name="staff-update"),
    path("staff/<int:pk>/delete/", StaffDeleteView.as_view(), name="staff-delete"),
    path("staff/<int:pk>/detail/", StaffDetailView.as_view(), name="staff-detail"),

    path("dishtype/create/", DishTypeCreateView.as_view(), name="dishtype-create"),
    path("dishtype/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dishtype-update"),
    path("dishtype/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dishtype-delete"),

    path("ingredient/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),

    path("home/", home, name="home"),
    path("dish-search/", dish_search, name="dish-search"),
    path("cook-search/", cook_search, name="cook-search"),
]
