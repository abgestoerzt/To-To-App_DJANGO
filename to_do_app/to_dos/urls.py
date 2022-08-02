
from django.urls import path


from to_dos.views import HomePageView, ToDoListView, ToDoDetailView

app_name = 'to-dos'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list', ToDoListView.as_view(), name='list'),
    path('to-do/<int:pk>', ToDoDetailView.as_view(), name='detail')

]
