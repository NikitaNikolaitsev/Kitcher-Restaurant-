from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from kitcherapp.forms import (
    CookCreateForm,
    CookSearchForm,
    DishForm,
    DishSearchForm,
    DishTypeForm,
)
from kitcherapp.models import Dish, Cook, DishType, Ingredient


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    context = {}
    return render(request, "kitcher/home_page.html", context=context)


def home(request):
    dish_search_form = DishSearchForm()
    cook_search_form = CookSearchForm()
    return render(request, 'home.html', {
        'dish_search_form': dish_search_form,
        'cook_search_form': cook_search_form
    })


def dish_search(request):
    form = DishSearchForm(request.GET)
    if form.is_valid():
        dishes = Dish.objects.all()

        if name := form.cleaned_data.get('name'):
            dishes = dishes.filter(name__icontains=name)

        if min_price := form.cleaned_data.get('min_price') is not None:
            dishes = dishes.filter(price__gte=min_price)

        if max_price := form.cleaned_data.get('max_price') is not None:
            dishes = dishes.filter(price__lte=max_price)
    else:
        dishes = Dish.objects.none()

    return render(request, 'search/dish_search_results.html', {'dishes': dishes, 'form': form})


@login_required(login_url='login')
def cook_search(request):
    form = CookSearchForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        job_title = form.cleaned_data.get('job_title')
        cooks = Cook.objects.all()
        if name:
            cooks = cooks.filter(first_name__icontains=name) | cooks.filter(last_name__icontains=name)
        if job_title:
            cooks = cooks.filter(job_title__icontains=job_title)
    else:
        cooks = Cook.objects.none()
    return render(request, 'search/cook_search_results.html', {'cooks': cooks, 'form': form})


class MenuView(generic.ListView):
    model = Dish
    template_name = "kitcher/menu/menu_view.html"
    context_object_name = "dishes"
    queryset = Dish.objects.all()
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context["dish_count"] = Dish.objects.count()
        return context


class MenuCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitcher:menu")
    template_name = "kitcher/menu/menu_create.html"


class MenuUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitcher:menu")
    template_name = "kitcher/menu/menu_create.html"


class MenuDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitcher:menu")
    template_name = "kitcher/menu/menu_delete.html"


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related("cooks")
    template_name = 'kitcher/menu/dish_detail.html'


class StaffBaseView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitcher/staff/staff.html"
    context_object_name = "cooks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cooks_by_job_title = {}
        for cook in self.get_queryset():
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
    success_url = reverse_lazy("kitcher:staff")


class StaffUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("kitcher:staff")
    template_name = "kitcher/staff/staff_create.html"


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitcher:staff")
    template_name = "kitcher/staff/staff_delete.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    fields = ['name']
    template_name = "kitcher/dish_type/dish_type_create.html"
    success_url = reverse_lazy("kitcher:dishtype-create")


class DishTypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = DishType
    fields = ['name']
    template_name = "kitcher/dish_type/dish_type_create.html"
    success_url = reverse_lazy("kitcher:dishtype-create")


class DishTypeDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitcher:dishtype-create")
    template_name = "kitcher/dish_type/dish_type_delete.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitcher:ingredient-create")
    template_name = "kitcher/menu/ingredient_create.html"


class IngredientUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitcher:ingredient-create")
    template_name = "kitcher/menu/ingredient_create.html"
