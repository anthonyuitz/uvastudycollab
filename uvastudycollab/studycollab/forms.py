from django import forms
from django.contrib.auth.models import User
from studycollab.models import studygroup, course

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class infoByClassForm(forms.Form):
	className = forms.CharField(max_length = 100, label = 'Class Name')

class loginForm(forms.Form):
	username = forms.CharField(max_length = 100, label = 'Username')
	password = forms.CharField(widget = forms.PasswordInput())
	nextURL = forms.CharField(label='next', max_length= 50, widget=forms.HiddenInput(), required=False)

class addGroupForm(forms.ModelForm):
	class Meta:
		model = studygroup
		fields = ['name', 'course', 'description']

class addDocumentForm(forms.Form):
	className = forms.ModelChoiceField(queryset=course.objects.all().order_by('department__name', 'number'))
	name = forms.CharField(label='Name of file', max_length=50)
	description = forms.CharField(widget = forms.Textarea)
	document = forms.FileField(label='Select a file')