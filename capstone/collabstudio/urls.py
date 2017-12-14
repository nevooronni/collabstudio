from django.conf.urls import url,include
from django.conf import settings#IMPORT SETTINGS
from django.conf.urls.static import static#USE STATIC FILES
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
	url('^$',views.index,name = 'index'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)