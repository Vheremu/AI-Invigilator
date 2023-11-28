from django.db import models
from django.urls import reverse
from groups.models import Group
# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=50,blank=False)
    code = models.CharField(unique=True,max_length=50,default='',blank=False)
    description = models.CharField(max_length=100,blank=True)
    group = models.ForeignKey(Group,null=True,related_name='Group',on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('exams_app:detail',kwargs={'pk':self.pk})
class Question(models.Model):
    question = models.CharField(max_length=300)
    id=models.IntegerField(null=False,default=1,primary_key=True)
    a = models.CharField(max_length=150,null=True)
    b = models.CharField(max_length=150,null=True)
    c = models.CharField(max_length=150,null=True)
    d = models.CharField(max_length=150,null=True)
    answer = models.CharField(max_length=1,default='a',null=True)
    exam = models.ForeignKey(Exam,null=True,related_name='questions',on_delete=models.SET_NULL)
    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('exams_app:list')
