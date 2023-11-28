from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.urls import reverse,reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.views import generic
from code import getUserProfileInfo,checkifMember,addGroupMember,deleteGroupMemberRequest,deleteGroupMember , createGroupMember
from django.shortcuts import render
from .forms import AddGroup
from groups.models import Group,GroupMember,GroupMemberRequest
# Create your views here.
def AddMember(request):
    data = request.POST.get('name')
    iddata = request.POST.get('id')
    newuser = addGroupMember(iddata)
    print(newuser)
    my_dict = {}
    return render(request,'groups/index.html',context=my_dict)
def creategroup(request):
    form = AddGroup()
    if request.method == 'POST':
        form = AddGroup(data=request.POST)
        if form.is_valid():
            group=form.save(commit=True)
            group = group.id
            userid=request.user.pk
            num=getUserProfileInfo(userid)
            user = num.id
            newgroupmemberpk = createGroupMember(user,group)
            return render(request,'groups/index.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'groups/group_form.html',{'form':form})
def Creategroup(request):
    print('hello world')
    my_dict = {}
    return render(request,'groups/group_form.html',context=my_dict)
class CreateGroup(CreateView):
    fields = ('name','description')
    model = Group
class CreateGroupMember(CreateView):
    fields = ('group','user')
    model = GroupMember
class SingleGroup(DetailView):
    context_object_name = 'group_details'
    model = Group
    template_name = 'groups/group_detail.html'
class MemberDetailView(DetailView):
    context_object_name = 'member_details'
    model = GroupMember
    template_name = 'groups/memberrequest_detail.html'
class MemberRequestDetailView(DetailView):
    context_object_name = 'memberrequest_details'
    model = GroupMemberRequest
    template_name = 'groups/memberrequest_detail.html'
class ListGroups(ListView):
    context_object_name = 'group_list'
    model = Group
def listGroups(request):
    groups = Group.objects.all()
    data = set()
    for group in groups:
        groupid = group.id
        userid=request.user.pk
        num=getUserProfileInfo(userid)
        result = checkifMember(num,groupid)
        if result:
            data.add(group)
    groups=data
    group_list={'group':groups,'data':data}
    return render(request,'groups/group_list.html',context=group_list)
class GroupUpdateView(UpdateView):
    context_object_name = 'group_update'
    fields=('name','description')
    model=Group
    template_name = 'groups/group_form.html'
class MemberUpdateView(UpdateView):
    context_object_name = 'member_update'
    fields=('group','user')
    model=GroupMember
    template_name = 'groups/groupmember_form.html'
class GroupDeleteView(DeleteView):
    context_object_name = 'group_details'
    model=Group
    success_url = reverse_lazy('groups_app:list')
def MemberDeleteView(request):
    data = request.POST.get('name')
    iddata = request.POST.get('id')
    print(data)
    print(iddata)
    deleteGroupMember(iddata)
    return render(request,'groups/index.html')
def MemberRequestDeleteView(request):
    data = request.POST.get('name')
    iddata = request.POST.get('id')
    print(data)
    print(iddata)
    deleteGroupMemberRequest(iddata)
    return render(request,'groups_app:index')

# def AddMember(request):
#     data = request.POST.get('name')
#     iddata = request.POST.get('id')
#     newuser = addGroupMember(iddata)
#     print(newuser)
#     my_dict = {}
#     return render(request,'index.html',context=my_dict)

class index(TemplateView):
    template_name = 'groups/index.html'
