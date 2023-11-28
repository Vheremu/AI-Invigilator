from django.contrib import admin
from groups.models import Group , GroupMember , GroupMemberRequest
# Register your models here.
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupMemberRequest)
