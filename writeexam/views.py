from django.shortcuts import render
from sittings.models import Sitting
# Create your views here.
def index(request):
    x=request.POST.get('id')
    sitting=Sitting.objects.get(id=x)

    my_dict = {'sitting':sitting,}
    return render(request,'writeexams/index.html',my_dict)
def systemcheck(request):
    return render(request,'writeexams/systemcheck.html')
def exam(request):
    return render(request,'writeexams/exam.html',my_dict)
