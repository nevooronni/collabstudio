from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTestClass(TestCase):
	'''
	test case for our profie class
	'''
	def setUp(self):
		'''
		setup method
		'''
		self.profile_one = Profile(bio = 'all in')#create an instance of the profile class for every test

	def test_instance(self):
		'''
		test the method
		'''
		self.assertTrue(isinstance(self.profile_one,Profile))
		#User.objects.all().delete()

	def test_retrieve_profiles(self):
		'''
		retrieves all profiles from the db
		'''
		all_profiles = Profile.retrieve_profiles()
		profiles = Profile.objects.all()
		self.assertTrue(len(all_profiles) == len(profiles))