from django.shortcuts import render
from django.views.generic import View , TemplateView
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
class registergroup(CreateView):
    fields = ('group','user')
    model = GroupMemberRequest
    success_url = reverse_lazy('index')
