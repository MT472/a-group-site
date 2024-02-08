from django.shortcuts import render,redirect
from .models import account
from .forms import accountForm


def signup(request):
    if request.method=='POST':
        user_account=accountForm(request.POST,request.FILES)
        if user_account.is_valid():
            user_account.save()
            return redirect('index')
    user_account=accountForm()
    return render(request,'myapp/form2.html',{'user_account':user_account})


def aboutus(request):
    return render(request,'myapp/aboutUs.html')

def login(request):
    return render(request,'myapp/form1.html')

def index(request):
    return render(request,'myapp/index.html')