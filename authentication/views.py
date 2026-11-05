from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import rest_framework 

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('authentication:profile')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request,user)
            return redirect('authentication:profile')
    else:
        form = AuthenticationForm()
    return render(request,"authentication/login.html",{"form":form})

@login_required
def profile_view(request): 
    return render(request,'authentication/profile.html',{'user':request.user})
