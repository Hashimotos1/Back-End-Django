from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import ModelForm
from .forms import MedForm, RemindForm
from .models import Medication, Reminder
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the medreminderapp index.")


def home_handler(request):
    context = {
        'name': 'Julie'
    }
    return render(request, 'home.html', context)


# def medications_handler(request):
#     #if this is a POST request to process form data
#     if request.method == 'POST':
#         #create a new form instance, populate with data from request
#         form = MedForm(request.Post)
#         if form.is_valid():
#
#             return HttpResponse('Thank you')
#
#     #create a blank form
#     else:
#         form = MedForm()
#
#
#     return render(request, 'medications.html', {'form': form})

def medications_handler(request):
    context = {
        'form': MedForm
    }
    return render(request, 'medications.html', context)

def add_medication_handler(request):
    form = MedForm(request.POST)
    if form.is_valid():
        medication = Medication(med_name=form.cleaned_data['med_name'], med_dose=form.cleaned_data['med_dose'],
                                med_freq=form.cleaned_data['med_freq'], med_route=form.cleaned_data['med_route'],
                                med_timing=form.cleaned_data['med_timing'])
        medication.save()
        messages.add_message(request, messages.SUCCESS, 'You have added medication successfully')
    return redirect('Medications')

def reminders_handler(request):
    context = {
        'form': RemindForm
    }
    return render(request, 'reminders.html', context)

def add_reminder_handler(request):
    form = RemindForm(request.POST)
    if form.is_valid():
        reminder = Reminder(med_name=form.cleaned_data['med_name'], reminder_time=form.cleaned_data['reminder_time'],
                            reminder_note=form.cleaned_data['reminder_note'])
        reminder.save()
        messages.add_message(request, messages.SUCCESS, 'You have added reminder successfully')
    return redirect('Reminders')

def history_handler(request):
    return render(request, 'history.html')

def login_handler(request):
    return render(request, 'login.html')
