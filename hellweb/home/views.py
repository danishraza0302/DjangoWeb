from django.shortcuts import render,HttpResponse
# Create your views here.

def index(request):
    return render(request,'a.html')

def club(request):
    return render(request,'club.html')
    
   # return HttpResponse("Yes, I got accesse")

def help(request):
    return render(request,'help.html')

def sell(request):
    return render(request,'sell.html')
   # return HttpResponse("We are happy to help you")