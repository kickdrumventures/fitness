from django.conf.urls import patterns, url

from workouts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^location/$', views.location, name='location'),
	url(r'^sessions/(?P<session_id>\d+)/add_set/$', views.add_set, name='add_set'),
	url(r'^sessions/(?P<session_id>\d+)/$', views.session_detail, name='session_detail'),
	url(r'^exercises/(?P<exercise_id>\d+)/$', views.exercise_detail, name='exercise_detail'),
	url(r'^exercises/add/$', views.add_exercises, name='add_exercises'),
	url(r'^exercises/$', views.exercises, name='exercises'),
	url(r'^weight/$', views.weight, name='weight'),
	url(r'^weight/add/$', views.add_weight, name='add_weight'),
	url(r'^weight/add_target/$', views.add_target_weight, name='add_target_weight'),
	url(r'^sessions/$', views.sessions, name='sessions'),
	url(r'^sessions/add/$', views.add_session, name='add_session'),
	url(r'^test/$', views.test, name='test'),
	
)

