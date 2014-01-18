from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms
from django.utils.timezone import utc
import datetime
import time
import pytz
from utils import unix_time_millis
from graphing import generate_session_graph, generate_exercise_detail_graph, generate_weight_graph
from django.contrib.auth.decorators import login_required

from workouts.models import Session, Set, ExerciseType, Exercise, Weight, WeightForm, SessionForm, SetForm, ExerciseForm, TargetWeight, TargetWeightForm, Location


@login_required
def test(request):
	return render(request, 'workouts/test.html', {})


@login_required
def index(request):
	all_exercises = Exercise.objects.all()
	try:
		last_weight = Weight.objects.filter(user=request.user.id).latest('date')
	except:
		last_weight = []
	try:
		last_workout = Session.objects.filter(user=request.user.id).latest('date')
		days_since_last_workout = datetime.datetime.utcnow().replace(tzinfo=utc) - last_workout.date
		#Saturate to 0 days (in case a future workout is entered)
		if (days_since_last_workout.days<0):
			days_since_last_workout = datetime.datetime.utcnow() - datetime.datetime.utcnow()
	except:
		last_workout = []
		days_since_last_workout = "n/a"

	return render(request, 'workouts/index.html', {'all_exercises': all_exercises, 'last_weight':last_weight, 'days_since_last_workout':days_since_last_workout, 'last_workout':last_workout})

@login_required
def location(request):
	return HttpResponse("This is the locations page")

@login_required
def exercises(request):
	exercises_by_type = {}
	all_exercises = Exercise.objects.all()
	for exercise in all_exercises:
		if exercise.exercise_type in exercises_by_type:
			exercises_by_type[exercise.exercise_type].append(exercise)
		else:
			exercises_by_type[exercise.exercise_type] = [exercise]

	return render(request, 'workouts/exercises.html', {'exercises_by_type':exercises_by_type})

@login_required
def add_exercises(request):
	if request.method == 'POST':
		form = ExerciseForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/workouts/exercises/')
	else:
		form = ExerciseForm()

	return render(request, 'workouts/add_exercises.html', {'form':form})

@login_required
def exercise_detail(request, exercise_id):
	try:
		exercise = Exercise.objects.get(pk=exercise_id)
	except Exercise.DoesNotExist:
		raise Http404

	weight_rep_data = []

	all_sets = exercise.set_set.all()
	for exercise_set in all_sets:
		weight_rep_data.append([unix_time_millis(exercise_set.session.date)  , float(exercise_set.weight_resistance) , float(exercise_set.reps_mins)])

	exercise_detail_graph = generate_exercise_detail_graph(weight_rep_data, str(exercise.name))

	return render(request, 'workouts/exercise_detail.html', {'exercise':exercise, 'all_sets':all_sets, 'exercise_detail_graph':exercise_detail_graph})

@login_required
def weight(request):
	#Handle the weight entries
	all_weight_entries = Weight.objects.all().filter(user=request.user.id).order_by('-date')
	recent_weight_data = []
	weight_list = []
	for entry in all_weight_entries:
		weight_list.append([time.mktime(entry.date.timetuple())*1000, float(entry.weight)])
		recent_weight_data.append([entry.date, entry.weight])

	#Handle the target weight entries
	all_target_weight_entries = TargetWeight.objects.all().filter(user=request.user.id).order_by('-date')
	recent_target_weight_data = []
	target_weight_list = []
	for entry in all_target_weight_entries:
		target_weight_list.append([time.mktime(entry.date.timetuple())*1000, float(entry.weight)])
		recent_target_weight_data.append([entry.date, entry.weight])

	graph_dict = generate_weight_graph(weight_list, target_weight_list)

	return render(request, 'workouts/weight.html', {'recent_weight_data':recent_weight_data, 'weight_list':weight_list, 'graph_dict':graph_dict, 'recent_target_weight_data':recent_target_weight_data})

@login_required
def sessions(request):
	#Get all the sessions and order them by date
	all_sessions = Session.objects.filter(user=request.user.id).order_by('-date')
	
	#Define the variables
	data_by_week_date = []
	data_by_week_marginal = []
	data_by_week_totals = []
	number_of_weeks = 20
	start_date = datetime.datetime.today() - datetime.timedelta(weeks=number_of_weeks)
	week_number = 0
	total_workouts = 0
	interval = datetime.timedelta(weeks=1).total_seconds()*1000
	
	#Cycle through data per week
	while week_number < number_of_weeks:
		#Determine the period start/end date
		period_start_date = start_date + datetime.timedelta(weeks=week_number)
		period_end_date = start_date + datetime.timedelta(weeks=week_number+1)

		#Figure out how many workouts were completed between the start and end dates
		workout_counter = 0
		for session in all_sessions:
			if (period_start_date.replace(tzinfo=utc) < session.date < period_end_date.replace(tzinfo=utc)):
				workout_counter += 1

		#Update the total workout counter
		total_workouts += workout_counter

		#Populate the data lists
		data_by_week_date.append((period_start_date).strftime("%b %d"))
		data_by_week_marginal.append(int(workout_counter))
		data_by_week_totals.append(int(total_workouts))
		
		#Increment the counter
		week_number += 1
	
	#Generate the graph content
	session_graph = generate_session_graph(data_by_week_date, data_by_week_marginal, data_by_week_totals)

	return render(request, 'workouts/sessions.html', {'all_sessions':all_sessions, 'session_graph':session_graph})

@login_required
def session_detail(request, session_id):
	#Define the local variables
	if request.method == 'POST':
		form = SetForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/workouts/sessions/' + session_id)

		else:
			raise Http404

	else:
		#Create the form
		#Set default values for the fields (0x0 for the rep/weight info is used so it can be ignored later in other filters)
		form = SetForm(initial={'session':session_id, 'user':request.user.id, 'reps_mins':0, 'weight_resistance':0})
		form.fields['session'].widget = forms.HiddenInput()
		form.fields['user'].widget = forms.HiddenInput()
		form.fields['reps_mins'].widget = forms.HiddenInput()
		form.fields['weight_resistance'].widget = forms.HiddenInput()

		try: 
			#Get the session
			session = Session.objects.get(pk=session_id, user=request.user.id)
			
			exercise_library = []
			#Get the full list of exercises
			for exercise_object in Exercise.objects.all():
				#exercise_library.append({'label': str(exercise_object.name), 'value': str(exercise_object.id)})
				exercise_library.append(str(exercise_object.name))


			#Create a dictionary to store each set in the session by exercise
			sets_by_exercise = {}
			for workout_set in session.set_set.all():
				if workout_set.exercise in sets_by_exercise:
					sets_by_exercise[workout_set.exercise].append([workout_set.reps_mins, workout_set.weight_resistance])
				else:
					sets_by_exercise[workout_set.exercise] = [[workout_set.reps_mins, workout_set.weight_resistance], ]


		except Session.DoesNotExist:
			raise Http404

	return render(request, 'workouts/session_detail.html', {'sets_by_exercise':sets_by_exercise, 'session':session, 'exercise_library':exercise_library, 'form':form})	

@login_required
def add_session(request):
	if request.method == 'POST':
		form = SessionForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/workouts/sessions/')
	else:
		form = SessionForm(initial={'user':request.user.id})
		form.fields['user'].widget = forms.HiddenInput()
		form.fields['location'].queryset = Location.objects.filter(user=request.user.id)

	return render(request, 'workouts/add_session.html', {'form':form})	

		
@login_required	
def add_weight(request):
	if request.method == 'POST':
		form = WeightForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/workouts/weight/')
	else:
		form = WeightForm(initial={'user':request.user.id})
		form.fields['user'].widget = forms.HiddenInput()

	return render(request, 'workouts/add_weight.html', {'form':form})

@login_required	
def add_target_weight(request):
	if request.method == 'POST':
		form = TargetWeightForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/workouts/weight/')
	else:
		form = TargetWeightForm(initial={'user':request.user.id})
		form.fields['user'].widget = forms.HiddenInput()

	return render(request, 'workouts/add_target_weight.html', {'form':form})

@login_required
def add_set(request, session_id):
	try: 
		session = Session.objects.get(pk=session_id, user=request.user.id)
	
		if request.method == 'POST':
			form = SetForm(request.POST)
			if form.is_valid():
				form.save()

				return HttpResponseRedirect('/workouts/sessions/'+ str(session.id) +'/')
		else:
			form = SetForm(initial={'session':session_id, 'user':request.user.id})
			form.fields['session'].widget = forms.HiddenInput()
			form.fields['user'].widget = forms.HiddenInput()

	except Session.DoesNotExist:
			raise Http404

	return render(request, 'workouts/add_set.html', {'form':form, 'session':session})



