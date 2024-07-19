from django.urls import path

from kitcherapp import views
from kitcherapp.views import index, MenuView, StaffBaseView

urlpatterns = [
    path("", index, name="index"),
    path("menu/", MenuView.as_view(), name="menu"),
    path('staff/', StaffBaseView.as_view(), name='staff'),
]

app_name = "kitcher"
