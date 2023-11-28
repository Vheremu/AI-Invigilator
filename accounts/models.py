from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registrationnumber = models.CharField(blank=True,max_length=50,unique=True)
    is_student = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
class StudentInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registrationnumber = models.CharField(blank=True,max_length=11,unique=True)
    phonenumber = models.CharField(blank=True,max_length=10,unique=False)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
class LecturerInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    idnumber = models.CharField(blank=True,max_length=11,unique=True)
    icnumber = models.CharField(blank=True,max_length=10,unique=False)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
