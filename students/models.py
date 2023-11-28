from django.db import models
from accounts.models import UserProfileInfo
# Create your models here.
class Student(models.Model):
    account = models.ForeignKey(UserProfileInfo,related_name='account',null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.account.user.username
    def get_absolute_url(self):
        return reverse('exams_app:detail',kwargs={'pk':self.pk})
