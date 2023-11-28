from django.db import models
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
from exams.models import Exam
from accounts.models import UserProfileInfo
User=get_user_model()
register = template.Library()
# Create your models here.
class Sitting(models.Model):
    name = models.CharField(blank=False,default='',max_length=100)
    id = models.IntegerField(null=False,default=1,primary_key=True,unique=True)
    description = models.TextField(blank=True,default='')
    exam = models.ForeignKey(Exam,null=True,related_name='exams',on_delete=models.SET_NULL)
    length = models.CharField(blank=True,default='',max_length=100)
    schedule = models.DateTimeField(verbose_name='schedule',null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('sittings_app:detail',kwargs={'pk':self.pk})
class Candidate(models.Model):
    sitting = models.ForeignKey(Sitting,null=True,related_name='candidates',on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfileInfo,null=True,related_name='user_sittings',on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.user.username
    def get_absolute_url(self):
        return reverse('sittings_app:list')
class CandidateRequests(models.Model):
    sitting = models.ForeignKey(Sitting,null=True,related_name='candidaterequests',on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfileInfo,null=True,related_name='user_sittingrequests',on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.user.username
    def get_absolute_url(self):
        return reverse('sittings_app:list')
