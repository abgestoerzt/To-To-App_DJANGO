from django import forms
from .models import To_Do


class ToDoForm(forms.ModelForm):
    class Meta:
        model = To_Do
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control me-2'}),
        }
