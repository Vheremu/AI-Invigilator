from django.contrib import admin
from accounts.models import UserProfileInfo,StudentInfo,LecturerInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(StudentInfo)
admin.site.register(LecturerInfo)