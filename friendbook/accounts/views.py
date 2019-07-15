from django.shortcuts import render
from .forms import Userform
# Create your views here.


def user_register(request):
    form =Userform(request.POST or None)
    if form.is_valid():
        pass


    context={
        'form':form
    }
    return render(request,'user_register.html',context)


def user_login(request):
    context={

    }
    return render(request,'user_login.html',context)


def user_otp(request):
    context={

    }
    return render(request,'user_otp.html',context)

def dashboard(request):
    context={

    }
    return render(request,'dashboard.html',context)

def user_profile(request):
    context={

    }
    return render(request,'profile.html',context)

def edit_profile(request):
    context={

    }
    return render(request,'edit_profile.html',context)



def user_changepassword(request):
    context={

    }
    return render(request,'changepassword.html',context)


def user_resetpassword(request):
    context={

    }
    return render(request,'resetpassword.html',context)



def user_logout(request):
    context={

    }
    return render(request,'logout.html',context)

