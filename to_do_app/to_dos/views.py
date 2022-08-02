from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import To_Do

# Create your views here.


class HomePageView(TemplateView):
    template_name = "base.html"


class ToDoListView(ListView):
    model = To_Do


class ToDoDetailView(DetailView):
    model = To_Do
