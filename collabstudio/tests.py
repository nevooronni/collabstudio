from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Tags,Project,Follow,Comments

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
		self.project_one = Project(caption = 'Trap back jumping!')

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
		all_projects = Project.retrieve_projects()
		projects = Project.objects.all()
		self.assertTrue(len(all_projects) == len(projects)) 


class TagsTestClass(TestCase):
	'''
	test case for Tags class
	'''
	def setUp(self):
		'''
		set up method
		'''
		self.tag_one = Tags(title = 'new')

	def test_instance(self):
		'''
		test the method
		'''
		self.assertTrue(isinstance(self.tag_one,Tags))

	def test_save_tag(self):
		'''
		saves tag to the db
		'''
		self.tag_one.save_tag()
		all_tags = Tags.objects.all()
		self.assertTrue(len(all_tags) > 0)


	def test_delete_tag(self):
		'''
		deletes tag from the db
		'''
		self.tag_one.save_tag()
		all_tags = Tags.objects.all()
		self.tag_one.delete_tag()
		self.assertTrue(len(all_tags) == 0)

	def test_retrieve_tags(self):
		'''
		retrieve all tags from the db
		'''
		self.tag_one.save_tag()
		db_tags = Tags.retrieve_tags()
		all_tags = Tags.objects.all()
		self.assertTrue(len(db_tags) == len(all_tags)) 

class FollowTestClass(TestCase):
	'''
	test the follow class
	'''
	def test_instance(self):
		'''
		tests to see if it was instantiated properly
		'''
		self.neville = User(username = 'nevooronni')
		self.neville.save()

		self.chelsea = User(username = 'chelsea')
		self.chelsea.save()

		self.new_profile = Profile(user=self.neville,bio='bla bla blab bla')
		self.follow = Follow(user=self.neville,profile=self.new_profile)

		self.assertTrue(isinstance(self.follow, Follow))

	def test_retrieve_following(self):
		'''
		test retrieve_following method
		'''
		self.neville = User(username = 'nevooronni')
		self.neville.save()

		self.chelsea = User(username = 'chelsea')
		self.chelsea.save()

		self.new_profile = Profile(user=self.neville,bio='bla bla blab bla')
		self.new_project = Project(user=self.neville,caption='bla bla bla bla bla')
		self.follow = Follow(user=self.neville,profile=self.new_profile)
		
		get_following = Follow.retrieve_following(self.neville.id)
		following = Follow.objects.all()

		self.assertTrue(len(get_following) == len(following))


class CommentsTestClass(TestCase):
	'''
	test comments class
	'''
	def setUp(self):
		'''
		setup method
		'''
		self.comment = Comments(comment = 'bla bla bla bla bla bla')

	def test_instance(self):
		'''
		test to see if the object is an instance of th comment class
		'''
		self.assertTrue(isinstance(self.comment, Comments))

	def test_retrieve_project_comments(self):
		'''
		test the retrieve+_post_comments methods
		'''
		self.neville = User(username = 'nevooronni')
		self.neville.save()

		self.chelsea = User(username = 'chelsea')
		self.chelsea.save()

		self.new_profile = Profile(user=self.neville,bio='bla bla blab bla')
		self.new_post = Project(user=self.neville,caption='bla bla bla bla bla')

		self.comment = Comments(project=self.new_post,comment='bla bla bla')

		get_comments = Comments.retrieve_project_comments(self.new_post.id)

		comments = Comments.objects.all()

		self.assertTrue(len(get_comments) == len(comments))

