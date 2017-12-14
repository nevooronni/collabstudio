from django.shortcuts import render
from django.conf.urls import url 
from django.http import HttpResponse
from .forms import NewsLetterForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

def index(request):
	# if request.method == 'POST':
	# 	# form = NewsLetterForm(request.POST)
	# 	# if form.is_valid():
	# 	# 	name = form.cleaned_data['Neville']
	# 	# 	email = form.cleaned_data['email']
	# 	# 	recipient = NewsLetterRecipients(name = name,email = email)
	# 	# 	recipient.save()
	# 	# 	send_welcome_email(name,email)
	# 	# 	HttpResponseRedirect()

	# 	# else:
	# 	# 	form = NewsLetterForm()

	return render(request,'all-app/index.html')


