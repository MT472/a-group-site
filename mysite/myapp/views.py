from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages



def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            if cd['password'] == cd['password2']:
                user.save()
                return redirect('login')
            else:
                form=SignupForm()
    else:
        form=SignupForm()
    return render(request,'myapp/form2.html',context={'form':form})

def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('invalid')
                messages.error(request,'نام کاربری یا رمز عبور اشتباه است')
    else:
        form =LoginForm()
    return render(request,'myapp/form1.html',{'form':form})
def user_logout(request):
    logout(request)
    return render(request,"myapp/logout.html")
def aboutus(request):
    return render(request,'myapp/aboutUs.html')

def Invalid(request):
    return render(request,'myapp/invalid.html')

    
def index(request):
    return render(request,'myapp/index.html')

def html(request):
    return render(request,'myapp/page1.html')

def css(request):
    return render(request,'myapp/page2.html')

def js(request):
    return render(request,'myapp/page3.html')

def dj(request):
    return render(request,'myapp/page4.html')

def python(request):
    return render(request,'myapp/page5.html')
