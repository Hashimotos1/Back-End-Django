from django.db import models
from django.forms import ModelForm
from .models import Medication, Reminder


class MedForm(ModelForm):
        class Meta:
                model = Medication
                fields = ['med_name', 'med_dose', 'med_freq', 'med_route', 'med_timing']

class RemindForm(ModelForm):
        class Meta:
                model = Reminder
                fields = ['med_name', 'reminder_time', 'reminder_note']
