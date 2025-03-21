from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','published_date']
        widgets={
            'published_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
        }