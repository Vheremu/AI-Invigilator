from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
from accounts.models import UserProfileInfo
User=get_user_model()
register = template.Library()
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True,default='')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('groups_app:detail',kwargs={'pk':self.pk})
class GroupMember(models.Model):
    group = models.ForeignKey(Group,null=True,related_name='memberships',on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfileInfo,null=True,related_name='user_groups',on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.user.username
    def get_absolute_url(self):
        return reverse('groups_app:list')
class GroupMemberRequest(models.Model):
    group = models.ForeignKey(Group,null=True,related_name='membershipsrequest',on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfileInfo,null=True,related_name='user_groupsrequest',on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.user.username
    def get_absolute_url(self):
        return reverse('groups_app:list')
