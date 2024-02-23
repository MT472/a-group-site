from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'myapp/form2.html',{'form':form})

def user_login(request):
    form=AuthenticationForm(data=request.POST)
    if request.method=='POST':
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,login)
            return redirect('index')
    else:
        form=AuthenticationForm()
    return render(request,'myapp/form1.html',{'form':form})

@login_required
def account_detail(request):
    return render(request,'myapp/account.html')

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
