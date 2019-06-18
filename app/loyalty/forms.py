from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserUpdateForm(forms.ModelForm):
		email = forms.EmailField()
		class Meta:
			model = CustomUser
			fields = ['first_name','last_name','email']
class ProfileUpdateForm(forms.ModelForm):
		class Meta:
			model = Profile
			fields = ['image']


			