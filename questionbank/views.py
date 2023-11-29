from django.shortcuts import render
from .models import Question
from django.urls import reverse,reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
class index(TemplateView):
    template_name = 'questionbank/index.html'
class QuestionListView(ListView):
    context_object_name = 'question_list'
    model = Question
def list(request):
    questions = Question.objects.all()
    print(questions)
    question_list={'questions':questions}
    return render(request,'questionbank/question_list.html',context=question_list)
class QuestionCreateView(CreateView):
    fields=('questionname','id','a','b','c','d','answer')
    model=Question
class QuestionDetailView(DetailView):
    context_object_name = 'question_details'
    model = Question
    template_name = 'questionbank/question_detail.html'
class QuestionUpdateView(UpdateView):
    context_object_name = 'question_update'
    fields=('questionname','id','a','b','c','d','answer')
    model=Question
    template_name = 'questionbank/question_form.html'
class QuestionDeleteView(DeleteView):
    context_object_name = 'question_details'
    model=Question
    success_url = reverse_lazy('questionbank_app:list')