from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from studycollab.forms import *
from studycollab.models import studygroup, document, course, help_category, help_question
from django.contrib.auth import authenticate, login as auth_login
import json
import re

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

def findInformation(request):
	if request.method == 'POST':
		form = infoByClassForm(request.POST)

		if form.is_valid():
			className = form.cleaned_data['className']
			classArr = re.split('(\d+)',className)
			studygroups = []
			documents = []
			if(len(classArr) > 1):
				studygroups = studygroup.objects.filter(course__department__code__iexact=classArr[0].strip().upper()).filter(course__number=classArr[1].strip()).distinct()
				documents = document.objects.filter(course__department__code__iexact=classArr[0].strip().upper()).filter(course__number=classArr[1].strip()).distinct()
				if studygroups or documents:
					return render(request,'browse.html', {'infoByClassForm' : form, 'associatedGroups' : studygroups, 'documents' : documents})
			return render(request, 'browse.html', {'infoByClassForm' : form, 'error' : 'No one has created a group or uploaded a study guide for this class.'})
		
		else:
			return render(request,'browse.html', {'infoByClassForm' : form})
	else:
		form = infoByClassForm()
		return render(request,'browse.html', {'infoByClassForm' : form})

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

def displayGroup(request, groupvalue):
	group = get_object_or_404(studygroup, groupid=groupvalue)
	return render(request, 'displayGroup.html', {'studygroup': group})

def addGroup(request):
	added = False
	if not request.user.is_authenticated():
		form = loginForm()
		return render(request, 'login.html', {'error' : 'Please login to use this feature.', 'form' : form})
	if request.method == 'POST':
		form = addGroupForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			submission.owner = request.user
			submission.save()
			form.save_m2m();
			added = True
		else:
			print(form.errors)
	else:
		form = addGroupForm()
	return render(request, 'addGroup.html',{'addGroupForm': form, 'added' : added})

def addDocument(request):
	added = False
	if not request.user.is_authenticated():
		form = loginForm()
		return render(request, 'login.html', {'error' : 'Please login to use this feature.', 'form' : form})
	if request.method == 'POST':
		form = addDocumentForm(request.POST, request.FILES)
		if form.is_valid():
			doc = document(course = course.objects.get(pk=request.POST['className']), name = request.POST['name'], 
				description = request.POST['description'], owner = request.user, document = request.FILES['document'])
			doc.save()
			added = True
	else:
		form = addDocumentForm()
	return render(request, 'addDocument.html',{'addDocumentForm': form, 'added' : added})

def displayHelp(request):
	helpcategories = help_category.objects.all().order_by('priority')
	helpquestions = help_question.objects.all().order_by('priority')
	return render(request, 'help.html', {'category': helpcategories, 'question': helpquestions})

		





