from django.shortcuts import render
from .forms import CookieForm

# Create your views here.
def theme(request):
    theme_cookie = request.COOKIES.get('theme','LT')#هربار کوکی خودکار ارسال می شود
    form = CookieForm()
    if request.method  == 'POST':
        form = CookieForm(request.POST)
        if form.is_valid():
            theme_choice = form.cleaned_data['theme']
            response = render(request, "cookie/cookie.html",{
                'form': form,
                'theme':theme_choice
                })
            response.set_cookie('theme',theme_choice,max_age=60*60*24*30)
            return response
    
    else:
        theme_choice = theme_cookie
    return render(request,'cookie/cookie.html',{
        'form':form,
        'theme':theme_choice
        })