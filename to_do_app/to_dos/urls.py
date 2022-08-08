
from django.urls import path


from to_dos.views import ToDoDetailView, ToDoUpdateView, ToDoCreateView, ToDoDelelteView, ToDoListView
from . import views


app_name = 'to-dos'

urlpatterns = [
    path('', ToDoListView.as_view(), name='home'),
    path('to-do/<int:pk>', ToDoDetailView.as_view(), name='detail'),
    path('to-do/edit/<int:pk>', ToDoUpdateView.as_view(), name='update'),
    path('create/', ToDoCreateView.as_view(), name='create'),
    path('to-do/delete/<int:pk>', ToDoDelelteView.as_view(), name='delete'),
    path('to-do/cross_off/<to_do_id>', views.cross_off, name='cross_off'),
    path('to-do/uncross/<to_do_id>', views.uncross, name='uncross'),






]
