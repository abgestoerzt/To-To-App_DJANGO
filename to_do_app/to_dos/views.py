from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy

from .models import To_Do

# Create your views here.


class HomePageView(TemplateView):
    template_name = "base.html"


class ToDoListView(ListView):
    model = To_Do


class ToDoDetailView(DetailView):
    model = To_Do


class ToDoUpdateView(UpdateView):
    model = To_Do
    fields = ['name', 'deadline', 'category']
    template_name_suffix = '_update_form'
    success_url = '/'  # this is not so nice, better use reverse or reverse lazy: https://stackoverflow.com/questions/66262282/how-to-redirect-an-updateview-upon-success


class ToDoCreateView(CreateView):
    model = To_Do
    fields = ['name', 'deadline', 'category']
    success_url = '/'


class ToDoDelelteView(DeleteView):
    model = To_Do
    success_url = reverse_lazy('to-dos:list')


def cross_off(request, to_do_id):
    item = To_Do.objects.get(pk=to_do_id)
    item.is_done = True
    item.save()
    return redirect('/')


def uncross(request, to_do_id):
    item = To_Do.objects.get(pk=to_do_id)
    item.is_done = False
    item.save()
    return redirect('/')
