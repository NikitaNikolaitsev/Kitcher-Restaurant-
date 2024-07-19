from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from kitcherapp.forms import RegisterForm
from kitcherapp.models import Dish, Cook, DishType


# Create your views here.


"""
BASIC STARTS VIEW
"""


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
    }
    return render(request, "kitcher/home_page.html", context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


"""
MENU STARTS VIEW
"""


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
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:dish-add")
    template_name = "kitcher/menu/menu_create.html"


class MenuUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:dish-add")
    template_name = "kitcher/menu/menu_create.html"


class MenuDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitcherapp:dish-add")
    template_name = "kitcher/menu/menu_delete.html"


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related("cooks")
    template_name = 'kitcher/menu/dish_detail.html'


"""
STAFF START VIEW
"""


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
    fields = "__all__"
    template_name = 'kitcher/staff/staff_create.html'
    success_url = reverse_lazy("kitcherapp:staff-create")


class StaffUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitcherapp:staff-create")
    template_name = "kitcher/staff/staff_create.html"


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitcherapp:staff-add")
    template_name = "kitcher/staff/staff_delete.html"


"""
DishTypE START VIEW
"""


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
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
