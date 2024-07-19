from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from kitcherapp.forms import RegisterForm
from kitcherapp.models import Dish, Cook


# Create your views here.


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


class MenuView(generic.ListView):
    model = Dish
    template_name = "kitcher/menu_view.html"
    context_object_name = "dishes"

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context["dish_count"] = Dish.objects.count()
        context["dish_all_info"] = Dish.objects.all()
        return context


class StaffBaseView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitcher/staff.html"
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
