from django.urls import path
from kitcherapp.views import index, MenuView, StaffBaseView, MenuUpdateView, MenuDeleteView, MenuCreateView, \
    DishDetailView, StaffDetailView, StaffUpdateView, StaffDeleteView, StaffCreateView, DishTypeCreateView, \
    DishTypeUpdateView, DishTypeDeleteView

urlpatterns = [
    path("", index, name="index"),

    path("menu/", MenuView.as_view(), name="menu"),
    path(
        "menu/create", MenuCreateView.as_view(), name="create-menu"
    ),
    path(
        "menu/<int:pk>/update", MenuUpdateView.as_view(), name="update-menu"
    ),
    path(
        "menu/<int:pk>/delete", MenuDeleteView.as_view(), name="delete-menu"
    ),
    path(
        "menu/<int:pk>/detail", DishDetailView.as_view(), name="dish-detail"
    ),

    path('staff/', StaffBaseView.as_view(), name='staff'),
    path(
        "staff/create", StaffCreateView.as_view(), name='staff-create'
    ),
    path(
        "staff/<int:pk>/update", StaffUpdateView.as_view(), name='staff-update'
    ),
    path(
        "staff/<int:pk>/delete", StaffDeleteView.as_view(), name='staff-delete'
    ),
    path(
        "staff/<int:pk>/detail", StaffDetailView.as_view(), name='staff-detail'
    ),

    path(
        'dishtype/create', DishTypeCreateView.as_view(), name='dishtype-create'
    ),
    path(
        'dishtype/<int:pk>/update', DishTypeUpdateView.as_view(), name='dishtype-update'
    ),
    path(
        'dishtype/<int:pk>/delete', DishTypeDeleteView.as_view(), name='dishtype-delete'
    ),
]

app_name = "kitcher"
