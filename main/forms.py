from .models import Langs
from django.forms import  ModelForm, TextInput, Textarea


class LangsForm(ModelForm):
    class Meta:
        model = Langs
        fields = ['title', 'langs']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input your Lang'
            }),
            "langs": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write the description'
            }),

        }