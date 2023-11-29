import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')
import django
from django.db.models import Q
from django.contrib.auth.models import User
django.setup()
import random
from students.models import Student
from django.contrib.auth.backends import BaseBackend
from accounts.models import UserProfileInfo,StudentInfo,LecturerInfo
from groups.models import Group,GroupMember,GroupMemberRequest
from sittings.models import Candidate,CandidateRequests,Sitting
# from faker import Faker
# fakegen = Faker()
# def populate(N=20):
#     for entry in range(N):
#         fake_name = fakegen.job()
#         fake_description = fakegen.text()
#         grp = Group.objects.get_or_create(name=fake_name,description=fake_description)[0]
# if __name__=='__main__':
#     print('population script is running' )
#     populate(20)
#     print('population complete')
def getpendingsitting(var):
    pendings = CandidateRequests.objects.get(id=var)
    print(pendings.sitting)
    pending = pendings
    pendings.save()
    return pending
def getpendingsittings(var):
    print('no pending')
    user = var
    pendingsittings = set()
    pendings = CandidateRequests.objects.all()
    print(pendings)
    for pending in pendings:
        if pending.user.user.username == user.user.username :
            print('match')
            pendingsittings.add(pending)
    print(pendingsittings)
    return pendingsittings
def getsittings(var):
    print('get sittings')
    sittings = Candidate.objects.all()
    sit = set()
    print(sittings)
    user = var
    for sitting in sittings:
        if sitting.user.user.username == user.user.username:
            print('match')
            sit.add(sitting)
    print(sit)
    return sit



def createStudent(UserProfileInfo):
    print('create student fn')
    user = UserProfileInfo
    students = Student.objects.all()
    exists = 0
    for student in students:
        if student.account.user.username == user.user.username:
            exists = 1
    exists = int(exists)
    if exists == 0 :
        Student.objects.create(account=user)
        print('student account was not existed so it was created')
        return 1
    else:
        print('student account already exists')
        return 0

def registersitting(UserProfileInfo,var):
    print('register fn')
    user = UserProfileInfo
    sittingid = str(var)
    sittings = Sitting.objects.all()
    print(sittings)
    for sitting in sittings:
        print(sitting.id)
        print(sittingid)

        if str(sitting.id) == sittingid:
            print('we have a match')
            print(sitting.name)
            request=CandidateRequests.objects.create(user=user,sitting=sitting)
            return 1
    return 0


def userfirsttime(var):
    return 0
def getLecturerInfo(var):
    try:
        user= LecturerInfo.objects.get(user=var)
    except:
        return 0


    return user
def getStudentInfo(var):
    try:
        user= StudentInfo.objects.get(user=var)
    except:
        return 0


    return user
def getUserProfileInfo(var):
    try:
        user= UserProfileInfo.objects.get(user=var)
    except:
        return 0


    return user
def checkifMember(UserProfileInfo,GroupId):
    user = UserProfileInfo
    group = Group.objects.get(id=GroupId)
    try:
        group.memberships.get(user=user)
        return 'is a lecturer'
    except:
        return 0
def checkIflecturer(UserProfileInfo):
    user = UserProfileInfo
    group = Group.objects.get(id=1)
    try:
        group.memberships.get(user=user)
        return 'is a lecturer'
    except:
        return 0
def deleteGroupMemberRequest(var):
    user = GroupMemberRequest.objects.get(id=var)
    text = str(user.user)
    print('deleted Group Member Request : '+text)
    user.delete()
    return 0
def deleteGroupMember(var):
    user = GroupMember.objects.get(id=var)
    text= str(user.user)
    print('deleted Group Member : '+text)
    user.delete()
    return 0
def createGroupMember(var1,var2):
    print(var1)
    print(var2)
    user = UserProfileInfo.objects.get(id=var1)
    group = Group.objects.get(id=var2)
    groupmember=GroupMember.objects.create(user=user,group=group)
    text = str(groupmember.user)
    print('created Group Member: '+text)
    return groupmember.pk
def createCandidate(var1,var2):
    print(var1)
    print(var2)
    user = UserProfileInfo.objects.get(id=var1)
    sitting = Sitting.objects.get(id=var2)
    candidate=Candidate.objects.create(user=user,sitting=sitting)
    text = str(candidate.user)
    print('created Candidate: '+text)
    return candidate.pk
def deleteCandidateRequest(var):
    user = CandidateRequests.objects.get(id=var)
    text= str(user.user)
    print('deleted Candidate Request : '+text)
    user.delete()
    return 0
def addCandidate(var):
    candidaterequest = CandidateRequests.objects.get(id=var)
    user= str(candidaterequest.user.id)
    sitting=str(candidaterequest.sitting.id)
    newgroupmemberpk = createCandidate(user,sitting)
    deleteolduser = deleteCandidateRequest(var)
    return 0
def addGroupMember(var):
    memberrequest = GroupMemberRequest.objects.get(id=var)
    user= str(memberrequest.user.id)
    group=str(memberrequest.group.id)
    newgroupmemberpk = createGroupMember(user,group)
    deleteolduser = deleteGroupMemberRequest(var)
    return 0
