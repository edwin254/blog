from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
	feedback = forms.CharField(widget=forms.Textarea, max_length = 450, required = True)

	class Meta:
		model = User
		fields = ['username','email']