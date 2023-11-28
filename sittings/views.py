from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from exams.forms import AddExam
from django.urls import reverse,reverse_lazy
from .models import Sitting,Candidate,CandidateRequests
from groups.models import Group
from code import addCandidate , getUserProfileInfo , checkifMember
# from sittings.models import Sitting , Candidate , CandidateRequests
# def AddMember(request):
#     data = request.POST.get('name')
#     iddata = request.POST.get('id')
#     newuser = addGroupMember(iddata)
#     print(newuser)
#     my_dict = {}
#     return render(request,'index.html',context=my_dict)
def AddCandidateView(request):
    data = request.POST.get('candidaterequestid')
    newuser = addCandidate(data)
    print(newuser)
    my_dict = {}
    return render(request,'sittings/index.html',context=my_dict)
class SittingListView(ListView):
    context_object_name = 'sitting_list'
    model = Sitting
def listSitting(request):
    userid=request.user.pk
    num=getUserProfileInfo(userid)
    groups = Group.objects.all()
    print(groups)
    sittings = Sitting.objects.all()
    data = set()
    sittingset = set()
    for group in groups:
        groupid = group.id
        userid=request.user.pk
        num=getUserProfileInfo(userid)
        result = checkifMember(num,groupid)
        if result:
            data.add(group)
    groups=data
    for sitting in sittings:
        sittinggroup=sitting.exam.group.id
        print(sittinggroup)
        for group in groups:
            if sitting.exam.group.id == group.id :
                sittingset.add(sitting)
    sittings=sittingset
    print(groups)
    print(sittings)
    sitting_list={'sittings':sittings}
    return render(request,'sittings/sitting_list.html',context=sitting_list)
# # class SingleGroup(DetailView):
# #     context_object_name = 'group_details'
# #     model = Group
# #     template_name = 'groups/group_detail.html'
class SittingDetailView(DetailView):
    context_object_name = 'sitting_details'
    model = Sitting
    template_name = 'sittings/sitting_detail.html'
class CandidateDetailView(DetailView):
    context_object_name = 'candidate_details'
    model = Candidate
    template_name = 'sittings/candidate_detail.html'
class CandidateRequestDetailView(DetailView):
    context_object_name = 'candidaterequest_details'
    model = CandidateRequests
    template_name = 'sittings/candidaterequest_detail.html'
class SittingCreateView(CreateView):
    fields=('name','id','description','exam','length','schedule')
    model=Sitting
class CandidateCreateView(CreateView):
    fields=('user','sitting')
    model=Candidate
class SittingUpdateView(UpdateView):
    context_object_name = 'sitting_update'
    fields=('name','id','description','exam','length','schedule')
    model=Sitting
    template_name = 'sittings/sitting_form.html'
class CandidateUpdateView(UpdateView):
    context_object_name = 'candidate_update'
    fields=('user','sitting')
    model=Candidate
    template_name = 'sittings/candidate_form.html'
# class QuestionUpdateView(UpdateView):
#     context_object_name = 'question_update'
#     fields=('question','id','a','b','c','d','answer','exam')
#     model=Question
#     template_name = 'exams/question_form.html'
class SittingDeleteView(DeleteView):
    context_object_name = 'sitting_details'
    model=Sitting
    success_url = reverse_lazy('sittings_app:list')
class CandidateDeleteView(DeleteView):
    context_object_name = 'candidate_details'
    model=Candidate
    success_url = reverse_lazy('sittings_app:list')
class CandidateRequestDeleteView(DeleteView):
    context_object_name = 'candidaterequest_details'
    model=CandidateRequests
    success_url = reverse_lazy('sittings_app:list')
# # class GroupUpdateView(UpdateView):
# #     context_object_name = 'group_update'
# #     fields=('name','description')
# #     model=Group
# #     template_name = 'groups/group_form.html'
# # class GroupDeleteView(DeleteView):
# #     context_object_name = 'group_details'
# #     model=Group
# #     success_url = reverse_lazy('groups_app:list')
class index(TemplateView):
    template_name = 'sittings/index.html'
