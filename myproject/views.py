from django.shortcuts import render
from django.views.generic import View , TemplateView
from accounts.models import StudentInfo,LecturerInfo
from groups.models import GroupMemberRequest
from django.urls import reverse,reverse_lazy
from django.views.generic import (CreateView)
from code import getUserProfileInfo,checkIflecturer
from django.contrib.auth import get_user_model
User=get_user_model()
# class index(TemplateView):
#     template_name = 'index.html'
def index(request):
    # data = request.POST.get('name')
    # iddata = request.POST.get('id')
    # newuser = addGroupMember(iddata)
    # print(newuser)
    if request.user.is_authenticated:
        print('user authenticated')
        try:
            student = StudentInfo.objects.get(user=request.user)
            print('student exists')
            return render(request,'studentsindex.html')
        except StudentInfo.DoesNotExist:
                print('student does not exist')
    else:
        print('user is not authenticated')
    if request.user.is_authenticated:
        print('user authenticated')
        try:
            lecturer = LecturerInfo.objects.get(user=request.user)
            print('lecturer exists')
            return render(request,'lecturersindex.html')
        except LecturerInfo.DoesNotExist:
                print('lecturer does not exist')
    else:
        print('user is not authenticated')
    if request.user.pk:
        num='registered user'
        user=request.user.pk
        num=getUserProfileInfo(user)
        lecturerscheck = checkIflecturer(num)
    else:
        num='not registered user'
        lecturerscheck = 'no user pk submited'

    my_dict = {'insert_me':num,'lecturers':lecturerscheck}
    return render(request,'index.html',context=my_dict)
def studentsindex(request):

   
    return render(request,'studentsindex.html')
class registergroup(CreateView):
    fields = ('group','user')
    model = GroupMemberRequest
    success_url = reverse_lazy('index')
