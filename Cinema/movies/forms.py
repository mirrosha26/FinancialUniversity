from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'genre', 'director', 'actors', 'description', 'duration')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'actors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
