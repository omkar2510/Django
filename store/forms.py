from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(forms.Form):
	class Meta:
		model = User
		fields = '__all__'	
	username = forms.CharField(error_messages={'required': 'Enter username'})
	email = forms.CharField(error_messages={'required': 'Enter email '})
	first_name = forms.CharField(error_messages={'required': 'Enter first name'})
	last_name = forms.CharField(error_messages={'required': 'Enter last name'})
	password = forms.CharField(error_messages={'required': 'Enter password'})
