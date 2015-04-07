from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class groupForm(forms.Form):
	className = forms.CharField(max_length = 100, label = 'Class Name')

class loginForm(forms.Form):
	username = forms.CharField(max_length = 100, label = 'Username')
	password = forms.CharField(widget = forms.PasswordInput())