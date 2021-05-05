from django.urls import path

from .views import home_handler, medications_handler, reminders_handler, history_handler, login_handler

from .views import SignUpView

urlpatterns = [
    path('', home_handler, name='Home'),
    path('medications', medications_handler, name='Medications'),
    path('reminders', reminders_handler, name='Reminders'),
    path('history', history_handler, name='History'),
    path('login', login_handler, name='Login'),
    path('signup/', SignUpView.as_view(), name='Signup')
]
