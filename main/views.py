from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm


def page(request):
    return render(request, 'main/page.html')


def python(request):
    notes = Notes.objects.order_by('title')
    return render(request, 'main/notes.html', {'title': 'NOTES TEMPLATE', 'notes': notes})


def add(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
        else:
            error = "You're wrote the wrong form"

    form = NotesForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)
