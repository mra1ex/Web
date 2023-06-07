from django.shortcuts import render, redirect
from .models import Peoples
from .forms import PeoplesForm

def general(request):
    return render(request, 'main/general.html')


def singup(request):

    return render(request, 'main/singup.html')


def singin(request):
    return render(request, 'main/singin.html')


def general1(request):
    return render(request, 'main/general1.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = PeoplesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general')
        else:
            error = 'Форма была неверной'
    form = PeoplesForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/general.html')

