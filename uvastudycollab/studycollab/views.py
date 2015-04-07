from django.shortcuts import render
from django.http import HttpResponse
from studycollab.forms import UserForm, groupForm
from studycollab.models import group
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
				if someGroup.className == className:
					groupJson = json.loads(someGroup.groups)
					associatedGroups = groupJson[className]
					return render(request,'findGroup.html', {'findGroupForm' : findGroupForm, 'associatedGroups' : associatedGroups})
			else:
				return HttpResponse("No one has created a group for your class") 

	else:
		findGroupForm = groupForm()
		associatedGroups = []
		return render(request,'findGroup.html', {'findGroupForm' : findGroupForm, 'associatedGroups' : associatedGroups})

