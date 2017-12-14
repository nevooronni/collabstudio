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

class ProjectTestClass(TestCase):
	'''
	test case for posts class
	'''
	def setUp(self):
		'''
		set up method
		'''
		self.project_one = Post(caption = 'Trap back jumping!')

	def test_instance(self):
		'''
		test the method
		'''
		self.assertTrue(isinstance(self.project_one,Project))	

	def test_retrieve_profile_projects(self):
		'''
		test for get posts for a specific profile
		'''
		self.neville = User(username = 'nevooronni')#create new user
		self.neville.save()#save new user

		self.chelsea = User(username = 'chelsea')#create another user
		self.chelsea.save()

		self.new_profile = Profile(user=self.neville,bio = 'bla bla blab bla')#create profile for user neville

		self.new_post = Project(user=self.neville,caption = 'bla bla bal bla')#create post for nevill profile

		retrieve_profile = Project.retrieve_profile_projects(self.neville.id)#get the profile post for profile neville

		profiles = Project.objects.all()#get all posts 

		self.assertTrue(len(retrieve_profile) == len(profiles))#since only profile exists(one we created) should be equla in lenghth retreived profile method 

	def test_retrieve_projects(self):
		'''
		test for retriving post from the db
		'''
		all_projects = Project.retrieve_project()
		projects = Project.objects.all()
		self.assertTrue(len(all_projects) == len(projects)) 