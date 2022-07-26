from django import forms
from pfour.models import user

class form1(forms.ModelForm):
    class Meta():
        model=user
        fields='__all__'
