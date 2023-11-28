from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from exams.forms import AddExam
from django.urls import reverse,reverse_lazy
from groups.models import Group
from exams.models import Exam,Question
from code import getUserProfileInfo,checkifMember,addGroupMember,deleteGroupMemberRequest,deleteGroupMember , createGroupMember

# Create your views here.
def AddExam_view(request):
    form = AddExam()
    if request.method == 'POST':
        form = AddExam(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'index.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'exams/addexam.html',{'form':form})
class ExamListView(ListView):
    context_object_name = 'exams_list'
    model = Exam
def listExams(request):
    userid=request.user.pk
    num=getUserProfileInfo(userid)
    groups = Group.objects.all()
    exams = Exam.objects.all()
    data = set()
    examset = set()
    for group in groups:
        groupid = group.id
        userid=request.user.pk
        num=getUserProfileInfo(userid)
        result = checkifMember(num,groupid)
        if result:
            data.add(group)
    groups=data
    for exam in exams:
        examid=exam.id
        for group in groups:
            if exam.group.id == group.id :
                examset.add(exam)
    examsets=examset
    exam_list={'examset':examsets,'data':examset}
    return render(request,'exams/exam_list.html',context=exam_list)
# class SingleGroup(DetailView):
#     context_object_name = 'group_details'
#     model = Group
#     template_name = 'groups/group_detail.html'
class ExamDetailView(DetailView):
    context_object_name = 'exam_details'
    model = Exam
    template_name = 'exams/exam_detail.html'
class QuestionDetailView(DetailView):
    context_object_name = 'question_details'
    model = Question
    template_name = 'exams/question_detail.html'
class ExamCreateView(CreateView):
    fields=('name','code','description','group')
    model=Exam
class QuestionCreateView(CreateView):
    fields=('question','id','a','b','c','d','answer','exam')
    model=Question
class ExamUpdateView(UpdateView):
    context_object_name = 'exam_update'
    fields=('name','code','description','group')
    model=Exam
    template_name = 'exams/exam_form.html'
class QuestionUpdateView(UpdateView):
    context_object_name = 'question_update'
    fields=('question','id','a','b','c','d','answer','exam')
    model=Question
    template_name = 'exams/question_form.html'
class ExamDeleteView(DeleteView):
    context_object_name = 'exam_details'
    model=Exam
    success_url = reverse_lazy('exams_app:list')
class QuestionDeleteView(DeleteView):
    context_object_name = 'question_details'
    model=Question
    success_url = reverse_lazy('exams_app:list')
# class GroupUpdateView(UpdateView):
#     context_object_name = 'group_update'
#     fields=('name','description')
#     model=Group
#     template_name = 'groups/group_form.html'
# class GroupDeleteView(DeleteView):
#     context_object_name = 'group_details'
#     model=Group
#     success_url = reverse_lazy('groups_app:list')
class index(TemplateView):
    template_name = 'exams/index.html'
