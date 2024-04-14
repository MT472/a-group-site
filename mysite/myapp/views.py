from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,LoginForm,EditUserForm
from django.contrib.auth import authenticate,login,logout,get_user_model
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

def check_username(request):
    username=request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red'>این نام کاربری قبلا توسط کاربر استفاده شده</div>")
    else:
        return HttpResponse("<div style='color:green'>این نام کاربری قابل استفاده است</div>")
    
def check_email(request):
    email=request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("<div style='color:red'>این ایمیل قبلا توسط کاربر استفاده شده</div>")
    else:
        return HttpResponse("<div style='color:green'>این ایمیل قابل استفاده است</div>")
def check_password(request):
    password=request.POST.get('password')
    if get_user_model().objects.filter(password=password).exists():
        return HttpResponse("<div style='color:red'>این رمز عبور قبلا توسط کاربر استفاده شده</div>")
    else:
        return HttpResponse("<div style='color:green'>این رمز عبور قابل استفاده است</div>")
    

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

def logout_user(request):
    logout(request)
    return render(request,'myapp/logout.html')

def aboutus(request):
    return render(request,'myapp/aboutUs.html')


def chat(request):
    return render(request,'myapp/chat.html')

@login_required
def edit_profile(request):
    if request.method=='POST':
        user_form=EditUserForm(instance=request.user,data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('confirm_edit')
    else:
        user_form=EditUserForm(instance=request.user)
    return render(request,'myapp/edit_profile.html',{'user_form':user_form})

def confirm_edit(request):
    return render(request,'myapp/edit.html')

def profile(request):
    return render(request,'myapp/profile.html')

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
