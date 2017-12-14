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

@login_required(login_url = '/accounts/login/')
def profile(request):
	current_user = request.user

	if current_user.is_authenticated():#check to see if current user is authenticated
		print('Logged In')
		posts = Post.objects.filter(user=current_user)#get post by current user
		profile = Profile.objects.filter(user=current_user)#get specific profile

		tags = Tags.retrieve_tags()

	current_user = request.user

	following = Follow.retrieve_following(current_user.id)#get following profiles 

	posts = Post.retrieve_posts()#get all posts 

	following_posts = []#empty array that will be for posts or the profiles you follow

	for follow in following:

		for post in posts:

			if follow.profile == post.profile:

				following_posts.append(post)


	return render(request, 'profile.html', {"posts":posts,"tags":tags,"profile":profile,"following":following,"user":current_user,"following_posts":following_posts})


