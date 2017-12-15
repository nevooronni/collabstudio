from django.conf.urls import url
from django.conf import settings#IMPORT SETTINGS
from django.conf.urls.static import static#USE STATIC FILES
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
	url('^$',views.index,name = 'index'),
	url('^accounts/profile/$',views.profile,name = 'profile'),
	url('^accounts/profile/update-profile/$',views.update_profile,name = 'update_profile'),
	url('^timeline/$',views.timeline,name = 'timeline'),
	url(r'^project/$',views.project,name = 'project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
