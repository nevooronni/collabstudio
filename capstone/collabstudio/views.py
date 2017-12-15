from django.shortcuts import render,redirect
from django.conf.urls import url 
from django.http import HttpResponse
from .forms import NewsLetterForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Tags,Follow,Comments
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import ProfileForm,NewProjectForm,ReviewForm


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
def index(request):
	return render(request,'all-app/index.html')

@login_required(login_url = '/accounts/login/')
def profile(request):
	current_user = request.user

	if current_user.is_authenticated:
		print('Logged In')
		project = Project.objects.filter(user=current_user)#get post by current user
		profile = Profile.objects.filter(user=current_user)#get specific profile

		tags = Tags.retrieve_tags()

	# current_user = request.user

	following = Follow.retrieve_following(current_user.id)#get following profiles 

	projects = Project.retrieve_projects()#get all posts 

	following_projects = []#empty array that will be for posts or the profiles you follow

	for follow in following:

		for project in projects:

			if follow.profile == project.profile:

				following_projects.append(project)


	return render(request, 'all-app/profile.html', {"projects":projects,"tags":tags,"profile":profile,"following":following,"user":current_user,"following_projects":following_projects})

@login_required(login_url = '/accounts/login/')
def update_profile(request):
	user = request.user

	if request.method == 'POST':
		profile_form = ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)
	
		if profile_form.is_valid():
			profile_form.save()
			return redirect(profile)

	else:	

		profile_form = ProfileForm(instance=request.user.profile)

	return render(request, 'all-app/update_profile.html',{"profile_form":profile_form,"user":user})

@login_required(login_url = '/accounts/login/')
def timeline(request):
	#profile section 
	try:
		current_user = request.user

		current_user_profile = current_user.profile

		profiles = Profile.retrieve_other_profiles(current_user.id)
	
	except objectDoesNotExist:
		raise Http404()

	#follow section 
	current_user = request.user

	following = Follow.retrieve_following(current_user.id)#get following profiles 

	projects = Projects.retrieve_posts()#get all posts 

	following_posts = []#empty array that will be for posts or the profiles you follow

	for follow in following:

		for project in projects:

			if follow.profile == project.profile:

				following_posts.append(project)

	return render(request, 'all-app/timeline.html',{"profiles":profiles,"following":following,"user":current_user,"following_projects":following_projects})

@login_required(login_url = '/accounts/login/')
def project(request):
	current_user = request.user
	current_profile = current_user.profile

	if request.method == 'POST':
		form = NewProjectForm(request.POST,request.FILES)

		if form.is_valid():
			project = form.save(commit=False)#commit your post
			project.user = current_user#post user should be current user
			project.profile = current_profile#post should be saved to curent_user profile
			project.save()#save the post 

			return redirect(profile)

		elif review_form.is_valid():
			print('the review form is working')

	else:

		form = NewProjectForm()

	return render(request, 'all-app/project.html', {"form":form,"current_user":current_user})

