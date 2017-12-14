from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Sum

#default images for profile
DEFAULT = 'profile/index.jpeg'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	website = models.CharField(max_length=30,blank=True)
	email = models.EmailField()
	phone_number = PhoneNumberField(max_length=10, blank=True)
	photo = models.ImageField(upload_to = 'profile/',blank=True,default=False)
	
	def __str__(self):
		return self.user.username

	# @classmethod
	# def one_profile(cls,id):
	# 	profile = Profile.objects.filter(user=user_id).all()
		
	@classmethod
	def retrieve_profiles(cls):
		all_profiles = Profile.objects.all().order_by('-id')
		return all_profiles

	@classmethod
	def retrieve_other_profiles(cls,user_id):
		profiles = Profile.objects.all()

		other_profiles = []

		for profile in profiles:

			if profile.user.id != user_id:
				other_profiles.append(profile)

		return other_profiles

	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

@property 
def photo_url(self):
	if self.photo and hasattr(self.photo, 'url'):
		return self.photo.url	