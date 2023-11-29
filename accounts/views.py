from django.shortcuts import render,redirect
from accounts.models import StudentInfo,LecturerInfo
from accounts.forms import UserForm,UserProfileInfoForm,StudentInfoForm,LecturerInfoForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('someone tried to login and failed')
            return HttpResponse('Invalid Credentials')


    else:
        return render(request,'accounts/login.html',{})
        print('hello')

def index(request):
    if request.user.is_authenticated:
        print(user)
        try:
            student = StudentInfo.objects.get(user=request.user)
            print('user exists')
        except StudentInfo.DoesNotExist:
                print('user does not exist')
    else:
        print('user is not authenticated')
    usertype=request.POST.get('user')
    return render(request,'index.html',{'usertype':usertype})
def prompt(request):
    return render(request,'accounts/prompt.html')
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors , profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'accounts/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def registerstudent(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        student_form = StudentInfoForm(data=request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            registered = True
        else:
            print(user_form.errors , student_form.errors)
    else:
        user_form = UserForm()
        student_form = StudentInfoForm()
    return render(request,'accounts/studentregistration.html',{'user_form':user_form,'student_form':student_form,'registered':registered})
def registerlecturer(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        lecturer_form = LecturerInfoForm(data=request.POST)
        if user_form.is_valid() and lecturer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            lecturer = lecturer_form.save(commit=False)
            lecturer.user = user
            if 'profile_pic' in request.FILES:
                lecturer.profile_pic = request.FILES['profile_pic']
            lecturer.save()
            registered = True
        else:
            print(user_form.errors , lecturer_form.errors)
    else:
        user_form = UserForm()
        lecturer_form = LecturerInfoForm()
    return render(request,'accounts/lecturerregistration.html',{'user_form':user_form,'lecturer_form':lecturer_form,'registered':registered})