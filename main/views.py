from django.shortcuts import render, redirect
from .models import Langs
from .forms import LangsForm


def page(request):
    return render(request, 'main/page.html')


def python(request):
    langs = Langs.objects.order_by('title')
    return render(request, 'main/python.html', {'title': 'LANGS TEMPLATE', 'langs': langs})

def add(request):
    error = ''
    if request.method == 'POST':
        form = LangsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('langs')
        else:
            error = "You're wrote the wrong form"

    form = LangsForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)