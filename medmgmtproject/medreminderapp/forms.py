from django.db import models
from django.forms import ModelForm
from .models import Medication

class MedForm(ModelForm):
        class Meta:
                model = Medication
                fields = ['med_name', 'med_dose', 'med_freq', 'med_route', 'med_timing']
        
