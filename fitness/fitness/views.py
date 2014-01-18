from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm


def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'login.html', c)

def auth_view(request):
	#Get the username and password from the form post
	#If no match, set to an empty string
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	#Check to see if there is a match for the user
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/workouts/')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def loggedin(request):
	return render(request, 'loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'invalid_login.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()

	return render(request, 'register.html', args)

def register_success(request):
	return render(request, 'register_success.html')