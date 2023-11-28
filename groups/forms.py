from django import forms
from .models import Group

class AddGroup(forms.ModelForm):
    class Meta():
        model = Group
        fields = '__all__'
