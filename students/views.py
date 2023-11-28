from django.shortcuts import render
import time,datetime
from code import deleteCandidateRequest,getpendingsitting,registersitting,getUserProfileInfo,createStudent,getpendingsittings,getsittings
from django.http import HttpResponseRedirect,HttpResponse
from sittings.models import CandidateRequests,Sitting,Candidate
from django.urls import reverse,reverse_lazy
from mytime import timeleft
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
def register(request):
    if request.method =='POST':
        form = request.POST
        id = form.get('id')
        userid=request.user.pk
        num=getUserProfileInfo(userid)
        print(id)
        k=registersitting(num,id)
        print(k)
        createStudent(num)
        if k==1:
            createStudent(num)
            return render(request,'students/mysittings.html')
        else:
            return HttpResponse('Invalid Registration Code')

    my_dict = {}
    return render(request,'students/register.html',context=my_dict)
class SittingRequestDeleteView(DeleteView):
    context_object_name = 'candidaterequest_details'
    model=CandidateRequests

    template_name = 'students/memberrequestdelete.html'
    success_url = reverse_lazy('students_app:mysittings')
def deletesittingrequest(request,pk):
    x=request.POST.get('delete')
    print(x)
    pendingsitting=getpendingsitting(pk)
    if x=='true' :
        print('hello')
        deleteCandidateRequest(pk)
        return render(request,'students/index.html')
    my_dict={'sitting':pendingsitting}
    return render(request,'students/memberrequestdelete.html',my_dict)
def mySittings(request):
    userid=request.user.pk
    num=getUserProfileInfo(userid)
    pendings=getpendingsittings(num)
    sittings = getsittings(num)
    print('mysittings app')
    my_dict = {'pendings':pendings,'sittings':sittings}
    return render(request,'students/mysittings.html',my_dict)
def sittingdetails(request,pk):
    candidate = Candidate.objects.get(id=pk)
    id=candidate.sitting.pk
    sitting = Sitting.objects.get(id=id)
    t = timeleft(sitting)
    write = int(round(t.total_seconds()))
    t = str(t)
    if (write >=1800):
        writes=1
    else:
        writes =0
    my_dict={'sitting':sitting,'time':t,'write':write,'writes':writes}
    return render(request,'students/sittingdetails.html',my_dict)
