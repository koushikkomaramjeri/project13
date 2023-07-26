from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'input.html')
def add(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    z=str(x+y)
    res=HttpResponse("data submitted successfully")
    res.set_cookie('c1',z,max_age=100)
    return res
def display(request):
    if 'c1' in request.COOKIES:
        r=request.COOKIES['c1']
        return HttpResponse("the sum is:"+r)
    else:
        return render(request,'input.html')
