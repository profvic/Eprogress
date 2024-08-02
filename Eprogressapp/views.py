from django.contrib import messages
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from Eprogressapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def showdemopage(request):
    return render(request, 'demo.html')

def showloginpage(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method!='POST':
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user!=None:
            login(request, user)  
            return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request, 'Invalid Login Details')
            return HttpResponseRedirect('/')
        
def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype :" +str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")
    

def Logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
