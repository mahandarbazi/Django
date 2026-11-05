from django.shortcuts import render,redirect
from .forms import AuthForm
from .models import Auth


def register_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['logged_in'] = True
            return redirect("profile")
    else:
        form = AuthForm()
        return render(request,'account/register.html',{'form':form})
    
def login_view(request):
    form = AuthForm() 
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd["name"]
            password = str(cd['password'])
            try:
                user = Auth.objects.get(name=name,password=password)
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['logged_in'] = True
                return redirect("profile")
            except Auth.DoesNotExist:
                form.add_error("کاربری یافت نشد",None)
    else:
        form = AuthForm()
    return render(request,'account/login.html',{"form":form})

def profile_view(request):
    try:
        user = Auth.objects.get(id=user.id)
    except Auth.DoesNotExist:
        request.session.flush()
        return redirect("login")
    return render(request,'account/profile.html',{"user":user})

def logout_view(request):
    request.session.flush()
    return redirect("login")
    