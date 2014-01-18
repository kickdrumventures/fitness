from django.db import models
from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User

class ExerciseType(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class Exercise(models.Model):
	name = models.CharField(max_length=50)
	description_short = models.CharField(max_length=100)
	description_long = models.CharField(max_length=300)
	exercise_type = models.ForeignKey(ExerciseType, null=True, default=None)
	def __unicode__(self):
		return self.name
	
class Location(models.Model):
	#Needs User info
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
		
class Session(models.Model):
	#Needs User info
	user = models.ForeignKey(User)
	location = models.ForeignKey(Location)
	date = models.DateTimeField('date of workout session')
	description = models.CharField(max_length=300)
	def __unicode__(self):
		return (str(self.location) + " - " + str(self.date.date()))
	
	
class Set(models.Model):
	#Needs User info
	user = models.ForeignKey(User)
	session = models.ForeignKey(Session)
	exercise = models.ForeignKey(Exercise, null=True, default=None)
	reps_mins = models.IntegerField()
	weight_resistance = models.IntegerField()
	def __unicode__(self):
		return (str(self.session) + " - " + str(self.exercise) + " - " + str(self.weight_resistance) + "x" +str(self.reps_mins))

class Weight(models.Model):
	#Needs User info
	user = models.ForeignKey(User)
	date = models.DateField('date of weighing')
	weight = models.DecimalField(max_digits=5, decimal_places=1)
	def __unicode__(self):
		return (str(self.date) + " - " + str(self.weight) + " lbs")	

class TargetWeight(models.Model):
	#Needs User info
	user = models.ForeignKey(User)
	date = models.DateField('date of weighing')
	weight = models.DecimalField(max_digits=5, decimal_places=1)
	def __unicode__(self):
		return (str(self.date) + " - " + str(self.weight) + " lbs")
	
class WeightForm(ModelForm):
	class Meta:
		model = Weight

class TargetWeightForm(ModelForm):
	class Meta:
		model = TargetWeight

class SessionForm(ModelForm):
	class Meta:
		model = Session
	

class SetForm(ModelForm):
	class Meta:
		model = Set

class ExerciseForm(ModelForm):
	class Meta:
		model = Exercise
	
