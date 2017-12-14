from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
	url('^$',views.index,name = 'index'),
]

if settings.DEBUG == True:
	urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)