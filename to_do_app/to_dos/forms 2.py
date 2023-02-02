from django import forms
from .models import To_Do


class To_Do_Form(forms.ModelForm):
    class Meta:
        model = To_Do
        fields = ["name"]
