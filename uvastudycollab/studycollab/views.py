from django.shortcuts import render
from django.http import HttpResponse
from studycollab.forms import UserForm, groupForm, loginForm
from studycollab.models import group
from django.contrib.auth import authenticate, login as auth_login
import json

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			registered=True

		else:
			print(user_form.errors)

	else:

		user_form = UserForm()

	return render(request, 'register.html',{'user_form': user_form, 'registered':registered})

def findGroup(request):
	if request.method == 'POST':
		findGroupForm = groupForm(request.POST)

		if findGroupForm.is_valid():
			className = findGroupForm.cleaned_data['className']

			groups = group.objects.all()
			for someGroup in groups:
				if someGroup.className.lower() == className.lower():
					groupJson = json.loads(someGroup.groups)
					associatedGroups = groupJson[someGroup.className]
					return render(request,'findGroup.html', {'findGroupForm' : findGroupForm, 'associatedGroups' : associatedGroups})
			return render(request, 'findGroup.html', {'error' : 'No one has created a group for this class.', 'findGroupForm' : findGroupForm});
		
		else:
			return render(request,'findGroup.html', {'findGroupForm' : findGroupForm})
	else:
		findGroupForm = groupForm()
		associatedGroups = []
		return render(request,'findGroup.html', {'findGroupForm' : findGroupForm, 'associatedGroups' : associatedGroups})

def login(request):
	if request.method == 'POST':
		form = loginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username = username, password = password)

			if user is not None and user.is_active:
				auth_login(request, user)
				return render(request, 'index.html', {'username' : username})
			else:
				return render(request, 'login.html', {'error' : 'Your username and password do not match, or your account is disabled. Please try again.', 'form' : form})
		else:
			return render(request, 'login.html', {'error' : 'The login could not be processed. Please check the errors below.','form' : form })
	else:
		form = loginForm()
		return render(request, 'login.html', {'form' : form })





