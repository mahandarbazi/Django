from django import forms
from .models import Auth

class AuthForm(forms.ModelForm):
    class Meta:
        model = Auth 
        fields = '__all__'
        labels = {
            'name':'UserName:',
            'password':'Password:'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
        error_messages = {
            'name' : { 
                'required':'Please Enter Your Username'
            },
            'password' : {
                 'required':'Please Enter Your Password'
            }
        }
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if Auth.objects.get(name=name).exists():
                raise forms.ValidationError("این نام کاربری قبلا ثبت نام شده است!")
