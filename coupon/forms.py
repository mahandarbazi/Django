from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    class Meta():
        model = Coupon
        fields = ['code']

        labels = {
            'code':'Code:'
        }
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control'})
        }
        error_messages = {
            'code':{
                'required':'لطفا کد تخفیف را وارد کنید',
            }
        }

        

    def clean_code(self):
        code =  self.cleaned_data.get('code')
        if not code:
            raise forms.ValidationError('کد تخفیف را وارد کنید:')
        try:
            coupon = Coupon.objects.get(code = code)
            if not coupon.active:
                raise forms.ValidationError('این کد تخفیف غیرغعال است')
            
        except Coupon.DoesNotExist:
            raise forms.ValidationError('کد تخفیف نامعتبر است.') 
        
        self.coupon_object = coupon
        return code
    



        
        
    