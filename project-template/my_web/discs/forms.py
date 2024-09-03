from django import forms
from .models import Disc


class DiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = ['name', 'type', 'brand', 'speed', 'glide', 'turn', 'fade', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter disc name'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
            'type': forms.Select(attrs={'class': 'form-control'}, choices=Disc.DISC_TYPES),
            'speed': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(1, 15)]),
            'glide': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(1, 7)]),
            'turn': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(-5, 2)]),
            'fade': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(0, 6)]),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),}


class DiscSearchForm(forms.Form):
    disc_name = forms.CharField(
        label='Disc name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for a disc'})
    )