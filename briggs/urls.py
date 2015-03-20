from django.conf.urls import patterns, url
from briggs import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^submit', views.submit, name='submit'),
	url(r'^view', views.view, name='view')
)
