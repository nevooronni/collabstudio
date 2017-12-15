from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Project,Comments

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio','website','phone_number','email','photo',)


class NewProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields=('photo','description',)

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comment',)

