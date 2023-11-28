from django import forms
from .models import Exam
class AddExam(forms.ModelForm):
    class Meta():
        model = Exam
        fields = '__all__'
