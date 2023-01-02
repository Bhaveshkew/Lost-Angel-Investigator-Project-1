from socket import fromshare
from django import forms
from calc.models import Person, User

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['image']


        