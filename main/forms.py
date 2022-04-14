from .models import Notes
from django.forms import  ModelForm, TextInput, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'langs']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input the name of your note'
            }),
            "langs": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write the note'
            }),

        }