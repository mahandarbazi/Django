from django import forms

class CookieForm(forms.Form):
    CHOICES = [
        ('DR', 'Dark'),
        ('LT', 'Light')
    ]
    theme = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    