from django.urls import path

from .views import home_handler, medications_handler, reminders_handler, history_handler, login_handler, \
    add_reminder_handler, add_medication_handler

urlpatterns = [
    path('', home_handler, name='Home'),
    path('medications', medications_handler, name='Medications'),
    path('add_reminder', add_medication_handler, name='Add Medication'),
    path('reminders', reminders_handler, name='Reminders'),
    path('add_reminder', add_reminder_handler, name='Add Reminder'),
    path('history', history_handler, name='History'),
    path('login', login_handler, name='Login')
]
