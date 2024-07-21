from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from kitcherapp.forms import (
    CookCreateForm,
    DishSearchForm,
    CookSearchForm,
    DishForm,
    DishSearchForm, DishTypeForm,
)
from kitcherapp.models import Dish, Cook, DishType, Ingredient

# Create your views here.


"""
BASIC STARTS VIEW
"""


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
    }
    return render(request, "kitcher/home_page.html", context=context)


"""
MENU STARTS VIEW
"""


def dish_search_view(request):
    form = DishSearchForm(request.GET or None)
    dishes = Dish.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        if name:
            dishes = dishes.filter(name__icontains=name)

    return render(request, 'kitcher/dish_search.html', {'form': form, 'dishes': dishes})


def dish_list_view(request):
    form = DishSearchForm(request.GET or None)
    dishes = Dish.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')

        if query:
            dishes = dishes.filter(
                name__icontains=query
            ) | dishes.filter(
                dish_type__name__icontains=query
            )

    return render(request, 'kitcher/dish_list.html', {'form': form, 'dishes': dishes})


class MenuView(generic.ListView):
    model = Dish
    template_name = "kitcher/menu/menu_view.html"
    context_object_name = "dishes"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context["dish_count"] = Dish.objects.count()
        context["dish_all_info"] = Dish.objects.all()
        return context


class MenuCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Dish
    form_class = DishForm
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:dish-create")
    template_name = "kitcher/menu/menu_create.html"


class MenuUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:dish-create")
    template_name = "kitcher/menu/menu_create.html"


class MenuDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitcherapp:menu")
    template_name = "kitcher/menu/menu_delete.html"


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related("cooks")
    template_name = 'kitcher/menu/dish_detail.html'


"""
STAFF START VIEW
"""


def cook_search_view(request):
    form = CookSearchForm(request.GET or None)
    cooks = Cook.objects.all()

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        years_of_experience = form.cleaned_data.get('years_of_experience')

        if first_name:
            cooks = cooks.filter(first_name__icontains=first_name)
        if last_name:
            cooks = cooks.filter(last_name__icontains=last_name)
        if username:
            cooks = cooks.filter(username__icontains=username)
        if years_of_experience is not None:
            cooks = cooks.filter(year_of_experience=years_of_experience)

    return render(request, 'kitcher/cook_search.html', {'form': form, 'cooks': cooks})


class StaffBaseView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitcher/staff/staff.html"
    context_object_name = "cooks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cooks_by_job_title = {}

        for cook in Cook.objects.all():
            if cook.job_title not in cooks_by_job_title:
                cooks_by_job_title[cook.job_title] = []
            cooks_by_job_title[cook.job_title].append(cook)
        context["cooks_by_job_title"] = cooks_by_job_title
        return context


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = 'kitcher/staff/staff_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StaffDetailView, self).get_context_data(**kwargs)
        cook = self.get_object()
        context['dishes'] = Dish.objects.filter(cooks=cook)
        return context


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreateForm
    template_name = 'kitcher/staff/staff_create.html'
    success_url = reverse_lazy("kitcherapp:staff-create")


class StaffUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("kitcherapp:staff-create")
    template_name = "kitcher/staff/staff_create.html"


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitcherapp:staff-create")
    template_name = "kitcher/staff/staff_delete.html"


"""
DishTypE START VIEW
"""


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form = DishTypeForm
    fields = ['name']
    template_name = "kitcher/dish_type/dish_type_create.html"
    success_url = reverse_lazy("kitcherapp:create-menu")


class DishTypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = DishType
    fields = ['name']
    template_name = "kitcher/dish_type/dish_type_create.html"
    success_url = reverse_lazy("kitcherapp:create-menu")


class DishTypeDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitcherapp:create-menu")
    template_name = "kitcher/dish_type/dish_type_delete.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:create-menu")
    template_name = "kitcher/menu/ingredient_create.html"


class IngredientUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:create-menu")
    template_name = "kitcher/menu/ingredient_create.html"
