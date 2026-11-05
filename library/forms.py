from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","pages","author","published_year"]

        labels = {
            "title":"Title:",
            "pages":"Pages:",
            "author":"Author:",
            "published_year":"Published:"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form"}),
            "pages":forms.NumberInput(attrs={"class":"form"}),
            "author":forms.Select(attrs={"class":"select"}),
            "published_year":forms.DateInput(attrs={"type":"date","class":"date"})
        }
        error_messages = {
            'title':{
                "required":"Please Enter the Title"
            },
            "pages":{
                "required":"Pleased Enter the Pages Number"
            },
            "author":{
                "required":"Please Enter the Author"
            },
            "published_year":{
                "required":"Please Enter the published_year"
            }
        }
    def clean(self):
        cleaned = super().clean()
        author = cleaned.get("author")
        year = cleaned.get("published_year")

        if author and year:
            if year.year < author.birth_year:
                raise forms.ValidationError("Published_year can not before author`s birth years")
            elif year.year > 2026:
                raise forms.ValidationError("published_year can not greater than this year ")
        return cleaned

