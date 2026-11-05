from django import forms
from django.core.validators import MaxLengthValidator
 

def start_with_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('this field should start with "s"')

class TeacherForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),min_length=9,label="Your Name:",
    error_messages={"min_length":"enter 12 character"},validators=[MaxLengthValidator(10),start_with_s])
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control mb-1'}),
    label='Your Email:',help_text="your email should be gmail address",initial='@gmail.com')

    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5',
    'placeholder':'enter your bio'}),label="Your Bio",label_suffix=':')

    
    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data['name']
    #     email = self.cleaned_data['email']
    #     if name[0].lower() != 's' and email[0].lower() != 's':
    #        raise forms.ValidationError('your name and email should start s')

    
    
    