from django.shortcuts import render,redirect
from .forms import CouponForm


# Create your views here.
def coupon_form(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            request.session['coupon_code'] = form.cleaned_data['code']
            request.session['coupon_object'] = {
                 'code':form.coupon_object.code,
                 'valid_from':form.coupon_object.valid_from.isoformat(),
                 'valid_to':form.coupon_object.valid_to.isoformat(),
                 'active':form.coupon_object.active
            }  
            return redirect('success')
    else:
            form = CouponForm()
    return render(request,'coupon/coupon_form.html',{'form':form})

def success(request):
     coupon_details = request.session.get('coupon_object',{})
     return render(request,'coupon/success.html',{'coupon':coupon_details})