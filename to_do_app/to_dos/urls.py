
from django.urls import path

from to_dos.views import HomePageView

app_name = 'to-dos'

urlpatterns = [
    path('', HomePageView.as_view(), name='home')

]
