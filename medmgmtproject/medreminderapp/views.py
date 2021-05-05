from django.shortcuts import render
from django.http import HttpResponse

from django.forms import ModelForm
from .forms import MedForm
from .models import Medication

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


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
    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
