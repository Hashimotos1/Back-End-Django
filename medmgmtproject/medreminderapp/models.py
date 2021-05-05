from django.db import models

#create User class model to map to the User database table
class User(models.Model):
	username = models.CharField(max_length=50, primary_key =True)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	age = models.IntegerField()
	height = models.IntegerField()
	weight = models.FloatField()

#create Medication class model to map to the Medication database table
class Medication(models.Model):
	med_name = models.CharField(max_length=25, primary_key=True)
	med_dose = models.CharField(max_length=15)
	med_freq = models.CharField(max_length=15)
	med_route = models.CharField(max_length=25)
	med_timing = models.CharField(max_length=25)

	def __str__(self):
		return self.med_name

#Create Reminder class model to map to the Reminder database table
class Reminder(models.Model):
	med_name = models.ForeignKey(Medication, on_delete=models.CASCADE)
	reminder_time = models.CharField(max_length=25)
	reminder_note = models.CharField(max_length=255)

	def __str__(self):
		return self.reminder_note
