from django.shortcuts import render
from django.http import HttpResponse
from pfour.forms import form1
# Create your views here.

def index(request):
    return render(request,'pfour/index.html')


def form(request):
    user1=form1()
    if request.method=='POST':
        user1=form1(request.POST)
        if user1.is_valid():
            user1.save()
            return index(request)
    return render(request,'pfour/form.html',{'user1':user1})

def other(request):
    newdi={'new':"hello"}
    return render(request,'pfour/other.html',context=newdi)
