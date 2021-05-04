from django.shortcuts import render
from django.http import HttpResponse

from django.forms import ModelForm
from .forms import MedForm
from .models import Medication


def index(request):
    return HttpResponse("Hello, world. You're at the medreminderapp index.")


def home_handler(request):
    context = {
        'name': 'Julie'
    }
    return render(request, 'home.html', context)


def medications_handler(request):
    #if this is a POST request to process form data
    if request.method == 'POST':
        #create a new form instance, populate with data from request
        form = MedForm(request.Post)
        if form.is_valid():
            
            return HttpResponse('Thank you')

    #create a blank form
    else:
        form = MedForm()
        

    return render(request, 'medications.html', {'form': form})
        


def reminders_handler(request):
    return render(request, 'reminders.html')


def history_handler(request):
    return render(request, 'history.html')


def login_handler(request):
    return render(request, 'login.html')
