from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo,StudentInfo,LecturerInfo
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password',)
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('registrationnumber','is_student','profile_pic')
        exclude =('user',)
class StudentInfoForm(forms.ModelForm):
    class Meta():
        model = StudentInfo
        fields = ('registrationnumber','phonenumber','profile_pic')
        exclude =('user',)
class LecturerInfoForm(forms.ModelForm):
    class Meta():
        model = LecturerInfo
        fields = ('idnumber','icnumber')
        exclude =('user',)
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
