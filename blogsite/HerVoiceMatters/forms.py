from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
	subject = forms.CharField(max_length= 60,required = False)
	message = forms.CharField(widget=forms.Textarea, max_length = 450, required = True)

	class Meta:
		model = User
		fields = ['username','email']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
     
	class Meta:
		model =User
		fields = ['username','password']

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password','password2']
	