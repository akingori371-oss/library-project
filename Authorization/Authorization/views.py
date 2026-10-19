from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import auth_login

def base(request):
    return render(request , "base.html")

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid:
            auth_login(request , form.get_user())
            return redirect('dashboard')
        else:
            form = AuthenticationForm()
    return render(request , "login.html" , {'form' : form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.method)
        if form.is_valid:
         form.save()
        return redirect("login.html")
    else:
        form = UserCreationForm()
    
    return render(request , "register.html")

def dashboard(request):
    return render(request , "dashboard.html")


    
   